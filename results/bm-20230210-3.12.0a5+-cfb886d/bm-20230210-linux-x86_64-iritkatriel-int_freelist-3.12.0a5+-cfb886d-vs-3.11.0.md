
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: cfb886d
- commit date: 2023-02-10
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| chameleon      | 6.41 ms                                                | 6.28 ms: 1.02x faster                                               |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                              |
| html5lib       | 63.2 ms                                                | 60.5 ms: 1.04x faster                                               |
| tornado_http   | 96.6 ms                                                | 94.2 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 71.9 ms: 1.06x faster                                               |
| pidigits       | 199 ms                                                 | 203 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                |
| regex_v8       | 22.3 ms                                                | 21.0 ms: 1.06x faster                                               |
| regex_effbot   | 3.36 ms                                                | 3.43 ms: 1.02x slower                                               |
| regex_dna      | 203 ms                                                 | 219 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.57 ms: 1.32x faster                                               |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.14x faster                                                |
| json_loads           | 26.2 us                                                | 23.8 us: 1.10x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                |
| pickle_pure_python   | 304 us                                                 | 287 us: 1.06x faster                                                |
| pickle_list          | 4.17 us                                                | 4.09 us: 1.02x faster                                               |
| pickle_dict          | 31.4 us                                                | 30.9 us: 1.02x faster                                               |
| unpickle_list        | 4.95 us                                                | 4.87 us: 1.02x faster                                               |
| xml_etree_iterparse  | 103 ms                                                 | 103 ms: 1.01x slower                                                |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                               |
| xml_etree_process    | 53.8 ms                                                | 55.7 ms: 1.04x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 80.8 ms: 1.06x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.92 ms: 1.07x slower                                               |
| python_startup_no_site | 5.96 ms                                                | 6.48 ms: 1.09x slower                                               |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 46.9 ms: 1.11x faster                                               |
| genshi_text     | 22.1 ms                                                | 20.6 ms: 1.07x faster                                               |
| mako            | 9.85 ms                                                | 9.81 ms: 1.00x faster                                               |
| django_template | 32.5 ms                                                | 33.1 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.57 ms: 1.32x faster                                               |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.14x faster                                                |
| deltablue               | 3.64 ms                                                | 3.20 ms: 1.14x faster                                               |
| genshi_xml              | 52.1 ms                                                | 46.9 ms: 1.11x faster                                               |
| json_loads              | 26.2 us                                                | 23.8 us: 1.10x faster                                               |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.02 ms: 1.10x faster                                               |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                                |
| scimark_fft             | 329 ms                                                 | 303 ms: 1.09x faster                                                |
| nqueens                 | 85.0 ms                                                | 79.1 ms: 1.08x faster                                               |
| genshi_text             | 22.1 ms                                                | 20.6 ms: 1.07x faster                                               |
| mdp                     | 2.62 sec                                               | 2.44 sec: 1.07x faster                                              |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                |
| hexiom                  | 6.35 ms                                                | 5.96 ms: 1.07x faster                                               |
| logging_silent          | 98.5 ns                                                | 92.4 ns: 1.07x faster                                               |
| sympy_str               | 287 ms                                                 | 270 ms: 1.06x faster                                                |
| regex_v8                | 22.3 ms                                                | 21.0 ms: 1.06x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                |
| go                      | 143 ms                                                 | 135 ms: 1.06x faster                                                |
| float                   | 76.3 ms                                                | 71.9 ms: 1.06x faster                                               |
| json                    | 4.95 ms                                                | 4.67 ms: 1.06x faster                                               |
| pickle_pure_python      | 304 us                                                 | 287 us: 1.06x faster                                                |
| richards                | 46.2 ms                                                | 43.6 ms: 1.06x faster                                               |
| deepcopy_memo           | 36.4 us                                                | 34.5 us: 1.06x faster                                               |
| pyflate                 | 417 ms                                                 | 395 ms: 1.05x faster                                                |
| fannkuch                | 388 ms                                                 | 368 ms: 1.05x faster                                                |
| sympy_integrate         | 20.9 ms                                                | 19.8 ms: 1.05x faster                                               |
| sympy_sum               | 166 ms                                                 | 157 ms: 1.05x faster                                                |
| logging_simple          | 6.06 us                                                | 5.77 us: 1.05x faster                                               |
| coverage                | 101 ms                                                 | 95.9 ms: 1.05x faster                                               |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                               |
| html5lib                | 63.2 ms                                                | 60.5 ms: 1.04x faster                                               |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                               |
| chaos                   | 68.6 ms                                                | 65.9 ms: 1.04x faster                                               |
| deepcopy                | 344 us                                                 | 330 us: 1.04x faster                                                |
| pycparser               | 1.17 sec                                               | 1.13 sec: 1.04x faster                                              |
| sqlglot_optimize        | 53.0 ms                                                | 51.1 ms: 1.04x faster                                               |
| pprint_pformat          | 1.44 sec                                               | 1.39 sec: 1.04x faster                                              |
| bench_thread_pool       | 810 us                                                 | 782 us: 1.04x faster                                                |
| raytrace                | 290 ms                                                 | 281 ms: 1.03x faster                                                |
| logging_format          | 6.62 us                                                | 6.41 us: 1.03x faster                                               |
| telco                   | 6.62 ms                                                | 6.42 ms: 1.03x faster                                               |
| sympy_expand            | 472 ms                                                 | 457 ms: 1.03x faster                                                |
| scimark_monte_carlo     | 68.3 ms                                                | 66.2 ms: 1.03x faster                                               |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                              |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                |
| tornado_http            | 96.6 ms                                                | 94.2 ms: 1.03x faster                                               |
| dulwich_log             | 63.9 ms                                                | 62.3 ms: 1.03x faster                                               |
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| pickle_list             | 4.17 us                                                | 4.09 us: 1.02x faster                                               |
| coroutines              | 26.1 ms                                                | 25.6 ms: 1.02x faster                                               |
| chameleon               | 6.41 ms                                                | 6.28 ms: 1.02x faster                                               |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                               |
| pickle_dict             | 31.4 us                                                | 30.9 us: 1.02x faster                                               |
| unpickle_list           | 4.95 us                                                | 4.87 us: 1.02x faster                                               |
| sqlalchemy_declarative  | 139 ms                                                 | 137 ms: 1.02x faster                                                |
| pprint_safe_repr        | 691 ms                                                 | 681 ms: 1.01x faster                                                |
| spectral_norm           | 99.9 ms                                                | 98.6 ms: 1.01x faster                                               |
| deepcopy_reduce         | 2.97 us                                                | 2.93 us: 1.01x faster                                               |
| mako                    | 9.85 ms                                                | 9.81 ms: 1.00x faster                                               |
| xml_etree_iterparse     | 103 ms                                                 | 103 ms: 1.01x slower                                                |
| thrift                  | 752 us                                                 | 758 us: 1.01x slower                                                |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                              |
| pidigits                | 199 ms                                                 | 203 ms: 1.02x slower                                                |
| django_template         | 32.5 ms                                                | 33.1 ms: 1.02x slower                                               |
| regex_effbot            | 3.36 ms                                                | 3.43 ms: 1.02x slower                                               |
| scimark_lu              | 107 ms                                                 | 110 ms: 1.03x slower                                                |
| sqlglot_transpile       | 1.66 ms                                                | 1.71 ms: 1.03x slower                                               |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.03x slower                                               |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                               |
| crypto_pyaes            | 73.9 ms                                                | 76.5 ms: 1.04x slower                                               |
| xml_etree_process       | 53.8 ms                                                | 55.7 ms: 1.04x slower                                               |
| generators              | 72.2 ms                                                | 75.4 ms: 1.04x slower                                               |
| async_tree_memoization  | 625 ms                                                 | 659 ms: 1.05x slower                                                |
| xml_etree_generate      | 76.2 ms                                                | 80.8 ms: 1.06x slower                                               |
| python_startup          | 8.36 ms                                                | 8.92 ms: 1.07x slower                                               |
| regex_dna               | 203 ms                                                 | 219 ms: 1.08x slower                                                |
| python_startup_no_site  | 5.96 ms                                                | 6.48 ms: 1.09x slower                                               |
| async_generators        | 359 ms                                                 | 429 ms: 1.19x slower                                                |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (8): async_tree_none, unpickle, unpack_sequence, bench_mp_pool, sqlalchemy_imperative, meteor_contest, nbody, async_tree_cpu_io_mixed
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy, pylint
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230210-3.12.0a5+-cfb886d/bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2
