
# Results vs. 3.11.0

- fork: brandtbucher
- ref: load_attr_class_from
- machine: linux-x86_64
- commit hash: 8b346a3
- commit date: 2023-01-16
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                         |
| chameleon      | 6.38 ms                                                | 6.33 ms: 1.01x faster                                                        |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                       |
| html5lib       | 64.8 ms                                                | 60.1 ms: 1.08x faster                                                        |
| tornado_http   | 96.5 ms                                                | 94.4 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.8 ms: 1.07x faster                                                        |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                         |
| nbody          | 90.0 ms                                                | 93.6 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                         |
| regex_effbot   | 3.46 ms                                                | 3.47 ms: 1.01x slower                                                        |
| regex_v8       | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                        |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.28 ms: 1.33x faster                                                        |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                         |
| pickle_pure_python   | 308 us                                                 | 272 us: 1.13x faster                                                         |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                         |
| json_loads           | 26.1 us                                                | 24.0 us: 1.09x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                         |
| pickle_dict          | 31.2 us                                                | 30.5 us: 1.02x faster                                                        |
| pickle_list          | 4.14 us                                                | 4.10 us: 1.01x faster                                                        |
| unpickle_list        | 4.99 us                                                | 5.03 us: 1.01x slower                                                        |
| xml_etree_process    | 53.7 ms                                                | 54.1 ms: 1.01x slower                                                        |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                        |
| xml_etree_generate   | 75.9 ms                                                | 78.4 ms: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.93 ms: 1.04x slower                                                        |
| python_startup_no_site | 6.04 ms                                                | 6.46 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                | 47.1 ms: 1.09x faster                                                        |
| genshi_text    | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                        |
| mako           | 9.83 ms                                                | 9.58 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 495 ms: 1.79x faster                                                         |
| json_dumps              | 12.4 ms                                                | 9.28 ms: 1.33x faster                                                        |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.97 ms: 1.15x faster                                                        |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                         |
| deltablue               | 3.66 ms                                                | 3.21 ms: 1.14x faster                                                        |
| pickle_pure_python      | 308 us                                                 | 272 us: 1.13x faster                                                         |
| crypto_pyaes            | 75.7 ms                                                | 67.2 ms: 1.13x faster                                                        |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                                         |
| scimark_monte_carlo     | 68.0 ms                                                | 62.1 ms: 1.10x faster                                                        |
| genshi_xml              | 51.4 ms                                                | 47.1 ms: 1.09x faster                                                        |
| richards                | 46.1 ms                                                | 42.3 ms: 1.09x faster                                                        |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                         |
| json_loads              | 26.1 us                                                | 24.0 us: 1.09x faster                                                        |
| scimark_fft             | 325 ms                                                 | 300 ms: 1.08x faster                                                         |
| sympy_str               | 291 ms                                                 | 269 ms: 1.08x faster                                                         |
| html5lib                | 64.8 ms                                                | 60.1 ms: 1.08x faster                                                        |
| nqueens                 | 83.8 ms                                                | 78.0 ms: 1.07x faster                                                        |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                         |
| float                   | 76.8 ms                                                | 71.8 ms: 1.07x faster                                                        |
| mdp                     | 2.63 sec                                               | 2.46 sec: 1.07x faster                                                       |
| unpack_sequence         | 44.5 ns                                                | 41.6 ns: 1.07x faster                                                        |
| json                    | 4.87 ms                                                | 4.57 ms: 1.07x faster                                                        |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                         |
| hexiom                  | 6.34 ms                                                | 5.98 ms: 1.06x faster                                                        |
| chaos                   | 68.7 ms                                                | 64.8 ms: 1.06x faster                                                        |
| logging_simple          | 6.02 us                                                | 5.69 us: 1.06x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 994 us: 1.06x faster                                                         |
| bench_thread_pool       | 817 us                                                 | 774 us: 1.06x faster                                                         |
| deepcopy_memo           | 35.8 us                                                | 34.0 us: 1.05x faster                                                        |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                         |
| genshi_text             | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                       |
| logging_silent          | 98.0 ns                                                | 93.6 ns: 1.05x faster                                                        |
| deepcopy                | 341 us                                                 | 326 us: 1.05x faster                                                         |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                        |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                                         |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                       |
| pprint_safe_repr        | 706 ms                                                 | 679 ms: 1.04x faster                                                         |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.04x faster                                                        |
| pyflate                 | 419 ms                                                 | 403 ms: 1.04x faster                                                         |
| pycparser               | 1.19 sec                                               | 1.14 sec: 1.04x faster                                                       |
| fannkuch                | 384 ms                                                 | 371 ms: 1.04x faster                                                         |
| sqlglot_optimize        | 52.7 ms                                                | 50.9 ms: 1.04x faster                                                        |
| coverage                | 99.3 ms                                                | 96.0 ms: 1.03x faster                                                        |
| coroutines              | 26.2 ms                                                | 25.3 ms: 1.03x faster                                                        |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                         |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                         |
| raytrace                | 291 ms                                                 | 283 ms: 1.03x faster                                                         |
| mako                    | 9.83 ms                                                | 9.58 ms: 1.03x faster                                                        |
| logging_format          | 6.48 us                                                | 6.31 us: 1.03x faster                                                        |
| dulwich_log             | 64.0 ms                                                | 62.5 ms: 1.02x faster                                                        |
| spectral_norm           | 98.1 ms                                                | 95.9 ms: 1.02x faster                                                        |
| deepcopy_reduce         | 3.02 us                                                | 2.95 us: 1.02x faster                                                        |
| tornado_http            | 96.5 ms                                                | 94.4 ms: 1.02x faster                                                        |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                         |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.02x faster                                                         |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                         |
| pickle_dict             | 31.2 us                                                | 30.5 us: 1.02x faster                                                        |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                        |
| thrift                  | 760 us                                                 | 745 us: 1.02x faster                                                         |
| async_generators        | 356 ms                                                 | 349 ms: 1.02x faster                                                         |
| pickle_list             | 4.14 us                                                | 4.10 us: 1.01x faster                                                        |
| chameleon               | 6.38 ms                                                | 6.33 ms: 1.01x faster                                                        |
| regex_effbot            | 3.46 ms                                                | 3.47 ms: 1.01x slower                                                        |
| unpickle_list           | 4.99 us                                                | 5.03 us: 1.01x slower                                                        |
| regex_v8                | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                        |
| xml_etree_process       | 53.7 ms                                                | 54.1 ms: 1.01x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                                       |
| telco                   | 6.43 ms                                                | 6.50 ms: 1.01x slower                                                        |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                        |
| async_tree_cpu_io_mixed | 736 ms                                                 | 756 ms: 1.03x slower                                                         |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                         |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                                        |
| xml_etree_generate      | 75.9 ms                                                | 78.4 ms: 1.03x slower                                                        |
| sqlite_synth            | 2.48 us                                                | 2.57 us: 1.03x slower                                                        |
| nbody                   | 90.0 ms                                                | 93.6 ms: 1.04x slower                                                        |
| sqlglot_parse           | 1.36 ms                                                | 1.42 ms: 1.04x slower                                                        |
| python_startup          | 8.58 ms                                                | 8.93 ms: 1.04x slower                                                        |
| generators              | 73.5 ms                                                | 77.2 ms: 1.05x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.46 ms: 1.07x slower                                                        |
| gc_traversal            | 3.82 ms                                                | 4.16 ms: 1.09x slower                                                        |
| dask                    | 365 ms                                                 | 501 ms: 1.37x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (7): djangocms, async_tree_none, django_template, bench_mp_pool, unpickle, meteor_contest, async_tree_memoization
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230116-3.12.0a4+-8b346a3/bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3.json: mypy
