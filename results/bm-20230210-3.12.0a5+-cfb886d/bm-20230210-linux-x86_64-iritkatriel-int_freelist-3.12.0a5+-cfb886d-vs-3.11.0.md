
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: cfb886d
- commit date: 2023-02-10
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| chameleon      | 6.38 ms                                                | 6.28 ms: 1.02x faster                                               |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                              |
| html5lib       | 64.8 ms                                                | 60.5 ms: 1.07x faster                                               |
| tornado_http   | 96.5 ms                                                | 94.2 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.9 ms: 1.07x faster                                               |
| pidigits       | 197 ms                                                 | 203 ms: 1.03x slower                                                |
| nbody          | 90.0 ms                                                | 95.4 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                |
| regex_v8       | 22.2 ms                                                | 21.0 ms: 1.06x faster                                               |
| regex_effbot   | 3.46 ms                                                | 3.43 ms: 1.01x faster                                               |
| regex_dna      | 203 ms                                                 | 219 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.57 ms: 1.29x faster                                               |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                |
| json_loads           | 26.1 us                                                | 23.8 us: 1.10x faster                                               |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                                |
| pickle_pure_python   | 308 us                                                 | 287 us: 1.07x faster                                                |
| unpickle_list        | 4.99 us                                                | 4.87 us: 1.02x faster                                               |
| pickle_list          | 4.14 us                                                | 4.09 us: 1.01x faster                                               |
| pickle_dict          | 31.2 us                                                | 30.9 us: 1.01x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                               |
| xml_etree_process    | 53.7 ms                                                | 55.7 ms: 1.04x slower                                               |
| xml_etree_generate   | 75.9 ms                                                | 80.8 ms: 1.06x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.92 ms: 1.04x slower                                               |
| python_startup_no_site | 6.04 ms                                                | 6.48 ms: 1.07x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.9 ms: 1.10x faster                                               |
| genshi_text     | 21.5 ms                                                | 20.6 ms: 1.05x faster                                               |
| mako            | 9.83 ms                                                | 9.81 ms: 1.00x faster                                               |
| django_template | 32.3 ms                                                | 33.1 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 496 ms: 1.78x faster                                                |
| json_dumps              | 12.4 ms                                                | 9.57 ms: 1.29x faster                                               |
| mypy2                   | 420 ms                                                 | 330 ms: 1.27x faster                                                |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.02 ms: 1.14x faster                                               |
| deltablue               | 3.66 ms                                                | 3.20 ms: 1.14x faster                                               |
| genshi_xml              | 51.4 ms                                                | 46.9 ms: 1.10x faster                                               |
| json_loads              | 26.1 us                                                | 23.8 us: 1.10x faster                                               |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.09x faster                                                |
| gc_traversal            | 3.82 ms                                                | 3.53 ms: 1.08x faster                                               |
| sympy_str               | 291 ms                                                 | 270 ms: 1.08x faster                                                |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                                |
| mdp                     | 2.63 sec                                               | 2.44 sec: 1.08x faster                                              |
| scimark_fft             | 325 ms                                                 | 303 ms: 1.08x faster                                                |
| pickle_pure_python      | 308 us                                                 | 287 us: 1.07x faster                                                |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                |
| html5lib                | 64.8 ms                                                | 60.5 ms: 1.07x faster                                               |
| float                   | 76.8 ms                                                | 71.9 ms: 1.07x faster                                               |
| hexiom                  | 6.34 ms                                                | 5.96 ms: 1.06x faster                                               |
| regex_v8                | 22.2 ms                                                | 21.0 ms: 1.06x faster                                               |
| logging_silent          | 98.0 ns                                                | 92.4 ns: 1.06x faster                                               |
| nqueens                 | 83.8 ms                                                | 79.1 ms: 1.06x faster                                               |
| pyflate                 | 419 ms                                                 | 395 ms: 1.06x faster                                                |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                               |
| richards                | 46.1 ms                                                | 43.6 ms: 1.06x faster                                               |
| pycparser               | 1.19 sec                                               | 1.13 sec: 1.05x faster                                              |
| sympy_sum               | 166 ms                                                 | 157 ms: 1.05x faster                                                |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                               |
| genshi_text             | 21.5 ms                                                | 20.6 ms: 1.05x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                              |
| bench_thread_pool       | 817 us                                                 | 782 us: 1.04x faster                                                |
| fannkuch                | 384 ms                                                 | 368 ms: 1.04x faster                                                |
| logging_simple          | 6.02 us                                                | 5.77 us: 1.04x faster                                               |
| chaos                   | 68.7 ms                                                | 65.9 ms: 1.04x faster                                               |
| json                    | 4.87 ms                                                | 4.67 ms: 1.04x faster                                               |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                |
| deepcopy_memo           | 35.8 us                                                | 34.5 us: 1.04x faster                                               |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                               |
| raytrace                | 291 ms                                                 | 281 ms: 1.04x faster                                                |
| pprint_safe_repr        | 706 ms                                                 | 681 ms: 1.04x faster                                                |
| coverage                | 99.3 ms                                                | 95.9 ms: 1.04x faster                                               |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.04x faster                                               |
| deepcopy                | 341 us                                                 | 330 us: 1.03x faster                                                |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                              |
| sqlglot_optimize        | 52.7 ms                                                | 51.1 ms: 1.03x faster                                               |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| deepcopy_reduce         | 3.02 us                                                | 2.93 us: 1.03x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                |
| dulwich_log             | 64.0 ms                                                | 62.3 ms: 1.03x faster                                               |
| scimark_monte_carlo     | 68.0 ms                                                | 66.2 ms: 1.03x faster                                               |
| unpack_sequence         | 44.5 ns                                                | 43.3 ns: 1.03x faster                                               |
| tornado_http            | 96.5 ms                                                | 94.2 ms: 1.03x faster                                               |
| unpickle_list           | 4.99 us                                                | 4.87 us: 1.02x faster                                               |
| coroutines              | 26.2 ms                                                | 25.6 ms: 1.02x faster                                               |
| chameleon               | 6.38 ms                                                | 6.28 ms: 1.02x faster                                               |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.01x faster                                               |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                                |
| pickle_list             | 4.14 us                                                | 4.09 us: 1.01x faster                                               |
| logging_format          | 6.48 us                                                | 6.41 us: 1.01x faster                                               |
| pickle_dict             | 31.2 us                                                | 30.9 us: 1.01x faster                                               |
| regex_effbot            | 3.46 ms                                                | 3.43 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| mako                    | 9.83 ms                                                | 9.81 ms: 1.00x faster                                               |
| crypto_pyaes            | 75.7 ms                                                | 76.5 ms: 1.01x slower                                               |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                              |
| scimark_lu              | 108 ms                                                 | 110 ms: 1.02x slower                                                |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                               |
| django_template         | 32.3 ms                                                | 33.1 ms: 1.02x slower                                               |
| generators              | 73.5 ms                                                | 75.4 ms: 1.03x slower                                               |
| async_tree_cpu_io_mixed | 736 ms                                                 | 755 ms: 1.03x slower                                                |
| pidigits                | 197 ms                                                 | 203 ms: 1.03x slower                                                |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                               |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                               |
| xml_etree_process       | 53.7 ms                                                | 55.7 ms: 1.04x slower                                               |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                               |
| python_startup          | 8.58 ms                                                | 8.92 ms: 1.04x slower                                               |
| async_tree_memoization  | 624 ms                                                 | 659 ms: 1.06x slower                                                |
| nbody                   | 90.0 ms                                                | 95.4 ms: 1.06x slower                                               |
| xml_etree_generate      | 75.9 ms                                                | 80.8 ms: 1.06x slower                                               |
| python_startup_no_site  | 6.04 ms                                                | 6.48 ms: 1.07x slower                                               |
| regex_dna               | 203 ms                                                 | 219 ms: 1.08x slower                                                |
| async_generators        | 356 ms                                                 | 429 ms: 1.21x slower                                                |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (9): sqlalchemy_imperative, thrift, unpickle, telco, async_tree_none, bench_mp_pool, meteor_contest, djangocms, spectral_norm
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, pylint
