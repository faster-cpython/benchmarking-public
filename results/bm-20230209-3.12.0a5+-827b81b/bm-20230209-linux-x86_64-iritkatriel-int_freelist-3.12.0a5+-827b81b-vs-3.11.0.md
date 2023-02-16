
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 827b81b
- commit date: 2023-02-09
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| docutils       | 2.60 sec                                               | 2.54 sec: 1.02x faster                                              |
| html5lib       | 64.8 ms                                                | 61.4 ms: 1.06x faster                                               |
| tornado_http   | 96.5 ms                                                | 93.9 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.0 ms: 1.05x faster                                               |
| pidigits       | 197 ms                                                 | 191 ms: 1.03x faster                                                |
| nbody          | 90.0 ms                                                | 94.5 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                                |
| regex_v8       | 22.2 ms                                                | 21.4 ms: 1.04x faster                                               |
| regex_dna      | 203 ms                                                 | 218 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.58 ms: 1.29x faster                                               |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.14x faster                                                |
| json_loads           | 26.1 us                                                | 24.0 us: 1.08x faster                                               |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                |
| pickle_pure_python   | 308 us                                                 | 289 us: 1.07x faster                                                |
| unpickle_list        | 4.99 us                                                | 4.88 us: 1.02x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| pickle_dict          | 31.2 us                                                | 31.2 us: 1.00x slower                                               |
| pickle_list          | 4.14 us                                                | 4.21 us: 1.02x slower                                               |
| xml_etree_process    | 53.7 ms                                                | 54.9 ms: 1.02x slower                                               |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                               |
| xml_etree_generate   | 75.9 ms                                                | 80.4 ms: 1.06x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.93 ms: 1.04x slower                                               |
| python_startup_no_site | 6.04 ms                                                | 6.47 ms: 1.07x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.1 ms: 1.09x faster                                               |
| genshi_text     | 21.5 ms                                                | 21.0 ms: 1.03x faster                                               |
| mako            | 9.83 ms                                                | 9.73 ms: 1.01x faster                                               |
| django_template | 32.3 ms                                                | 33.6 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 498 ms: 1.78x faster                                                |
| json_dumps              | 12.4 ms                                                | 9.58 ms: 1.29x faster                                               |
| mypy2                   | 420 ms                                                 | 330 ms: 1.27x faster                                                |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.99 ms: 1.15x faster                                               |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.14x faster                                                |
| deltablue               | 3.66 ms                                                | 3.22 ms: 1.13x faster                                               |
| genshi_xml              | 51.4 ms                                                | 47.1 ms: 1.09x faster                                               |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.09x faster                                              |
| json_loads              | 26.1 us                                                | 24.0 us: 1.08x faster                                               |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                |
| sympy_str               | 291 ms                                                 | 270 ms: 1.08x faster                                                |
| scimark_fft             | 325 ms                                                 | 302 ms: 1.08x faster                                                |
| nqueens                 | 83.8 ms                                                | 78.1 ms: 1.07x faster                                               |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                                |
| pickle_pure_python      | 308 us                                                 | 289 us: 1.07x faster                                                |
| richards                | 46.1 ms                                                | 43.3 ms: 1.06x faster                                               |
| hexiom                  | 6.34 ms                                                | 5.97 ms: 1.06x faster                                               |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                               |
| fannkuch                | 384 ms                                                 | 364 ms: 1.06x faster                                                |
| html5lib                | 64.8 ms                                                | 61.4 ms: 1.06x faster                                               |
| mdp                     | 2.63 sec                                               | 2.49 sec: 1.05x faster                                              |
| unpack_sequence         | 44.5 ns                                                | 42.3 ns: 1.05x faster                                               |
| float                   | 76.8 ms                                                | 73.0 ms: 1.05x faster                                               |
| logging_silent          | 98.0 ns                                                | 93.2 ns: 1.05x faster                                               |
| sympy_sum               | 166 ms                                                 | 158 ms: 1.05x faster                                                |
| json                    | 4.87 ms                                                | 4.64 ms: 1.05x faster                                               |
| logging_simple          | 6.02 us                                                | 5.74 us: 1.05x faster                                               |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                               |
| chaos                   | 68.7 ms                                                | 65.6 ms: 1.05x faster                                               |
| deepcopy_memo           | 35.8 us                                                | 34.2 us: 1.05x faster                                               |
| bench_thread_pool       | 817 us                                                 | 785 us: 1.04x faster                                                |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                |
| regex_v8                | 22.2 ms                                                | 21.4 ms: 1.04x faster                                               |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.04x faster                                               |
| deepcopy                | 341 us                                                 | 329 us: 1.04x faster                                                |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                               |
| sympy_expand            | 475 ms                                                 | 459 ms: 1.03x faster                                                |
| deepcopy_reduce         | 3.02 us                                                | 2.92 us: 1.03x faster                                               |
| pidigits                | 197 ms                                                 | 191 ms: 1.03x faster                                                |
| scimark_monte_carlo     | 68.0 ms                                                | 65.9 ms: 1.03x faster                                               |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| tornado_http            | 96.5 ms                                                | 93.9 ms: 1.03x faster                                               |
| pyflate                 | 419 ms                                                 | 407 ms: 1.03x faster                                                |
| genshi_text             | 21.5 ms                                                | 21.0 ms: 1.03x faster                                               |
| dulwich_log             | 64.0 ms                                                | 62.4 ms: 1.03x faster                                               |
| coroutines              | 26.2 ms                                                | 25.5 ms: 1.03x faster                                               |
| docutils                | 2.60 sec                                               | 2.54 sec: 1.02x faster                                              |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.02x faster                                              |
| unpickle_list           | 4.99 us                                                | 4.88 us: 1.02x faster                                               |
| raytrace                | 291 ms                                                 | 286 ms: 1.02x faster                                                |
| logging_format          | 6.48 us                                                | 6.36 us: 1.02x faster                                               |
| sqlglot_optimize        | 52.7 ms                                                | 51.7 ms: 1.02x faster                                               |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.8 ms: 1.02x faster                                               |
| coverage                | 99.3 ms                                                | 97.9 ms: 1.01x faster                                               |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.01x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                                |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                                |
| mako                    | 9.83 ms                                                | 9.73 ms: 1.01x faster                                               |
| pprint_safe_repr        | 706 ms                                                 | 699 ms: 1.01x faster                                                |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| pickle_dict             | 31.2 us                                                | 31.2 us: 1.00x slower                                               |
| gc_traversal            | 3.82 ms                                                | 3.85 ms: 1.01x slower                                               |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                              |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.01x slower                                                |
| pickle_list             | 4.14 us                                                | 4.21 us: 1.02x slower                                               |
| xml_etree_process       | 53.7 ms                                                | 54.9 ms: 1.02x slower                                               |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                               |
| async_tree_cpu_io_mixed | 736 ms                                                 | 755 ms: 1.03x slower                                                |
| crypto_pyaes            | 75.7 ms                                                | 77.7 ms: 1.03x slower                                               |
| scimark_lu              | 108 ms                                                 | 111 ms: 1.03x slower                                                |
| async_tree_memoization  | 624 ms                                                 | 649 ms: 1.04x slower                                                |
| python_startup          | 8.58 ms                                                | 8.93 ms: 1.04x slower                                               |
| django_template         | 32.3 ms                                                | 33.6 ms: 1.04x slower                                               |
| sqlglot_transpile       | 1.65 ms                                                | 1.73 ms: 1.05x slower                                               |
| sqlglot_parse           | 1.36 ms                                                | 1.43 ms: 1.05x slower                                               |
| nbody                   | 90.0 ms                                                | 94.5 ms: 1.05x slower                                               |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                               |
| generators              | 73.5 ms                                                | 77.7 ms: 1.06x slower                                               |
| xml_etree_generate      | 75.9 ms                                                | 80.4 ms: 1.06x slower                                               |
| python_startup_no_site  | 6.04 ms                                                | 6.47 ms: 1.07x slower                                               |
| regex_dna               | 203 ms                                                 | 218 ms: 1.07x slower                                                |
| async_generators        | 356 ms                                                 | 424 ms: 1.19x slower                                                |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (9): unpickle, thrift, djangocms, bench_mp_pool, async_tree_none, chameleon, regex_effbot, spectral_norm, telco
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, pylint
