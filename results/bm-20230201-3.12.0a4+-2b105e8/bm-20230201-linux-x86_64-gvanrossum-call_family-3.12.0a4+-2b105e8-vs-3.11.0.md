
# Results vs. 3.11.0

- fork: gvanrossum
- ref: call_family
- machine: linux-x86_64
- commit hash: 2b105e8
- commit date: 2023-02-01
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.04x faster                                              |
| chameleon      | 6.38 ms                                                | 6.42 ms: 1.01x slower                                             |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                            |
| html5lib       | 64.8 ms                                                | 59.4 ms: 1.09x faster                                             |
| tornado_http   | 96.5 ms                                                | 94.3 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.8 ms: 1.05x faster                                             |
| pidigits       | 197 ms                                                 | 198 ms: 1.00x slower                                              |
| nbody          | 90.0 ms                                                | 94.5 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.08x faster                                              |
| regex_v8       | 22.2 ms                                                | 21.5 ms: 1.03x faster                                             |
| regex_dna      | 203 ms                                                 | 213 ms: 1.05x slower                                              |
| regex_effbot   | 3.46 ms                                                | 3.62 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.40 ms: 1.31x faster                                             |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                              |
| json_loads           | 26.1 us                                                | 23.8 us: 1.10x faster                                             |
| pickle_pure_python   | 308 us                                                 | 283 us: 1.09x faster                                              |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                              |
| pickle_list          | 4.14 us                                                | 3.99 us: 1.04x faster                                             |
| pickle_dict          | 31.2 us                                                | 30.6 us: 1.02x faster                                             |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                              |
| xml_etree_process    | 53.7 ms                                                | 53.3 ms: 1.01x faster                                             |
| unpickle_list        | 4.99 us                                                | 5.03 us: 1.01x slower                                             |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                             |
| xml_etree_generate   | 75.9 ms                                                | 77.2 ms: 1.02x slower                                             |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                      |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.95 ms: 1.04x slower                                             |
| python_startup_no_site | 6.04 ms                                                | 6.48 ms: 1.07x slower                                             |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.2 ms: 1.11x faster                                             |
| genshi_text     | 21.5 ms                                                | 20.8 ms: 1.03x faster                                             |
| mako            | 9.83 ms                                                | 9.73 ms: 1.01x faster                                             |
| django_template | 32.3 ms                                                | 32.1 ms: 1.01x faster                                             |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 495 ms: 1.78x faster                                              |
| json_dumps              | 12.4 ms                                                | 9.40 ms: 1.31x faster                                             |
| deltablue               | 3.66 ms                                                | 3.13 ms: 1.17x faster                                             |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                              |
| genshi_xml              | 51.4 ms                                                | 46.2 ms: 1.11x faster                                             |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.13 ms: 1.11x faster                                             |
| richards                | 46.1 ms                                                | 41.8 ms: 1.10x faster                                             |
| json_loads              | 26.1 us                                                | 23.8 us: 1.10x faster                                             |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.09x faster                                              |
| html5lib                | 64.8 ms                                                | 59.4 ms: 1.09x faster                                             |
| chaos                   | 68.7 ms                                                | 63.0 ms: 1.09x faster                                             |
| pickle_pure_python      | 308 us                                                 | 283 us: 1.09x faster                                              |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                              |
| nqueens                 | 83.8 ms                                                | 77.3 ms: 1.08x faster                                             |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                            |
| sympy_str               | 291 ms                                                 | 270 ms: 1.08x faster                                              |
| regex_compile           | 136 ms                                                 | 127 ms: 1.08x faster                                              |
| logging_silent          | 98.0 ns                                                | 91.1 ns: 1.08x faster                                             |
| coroutines              | 26.2 ms                                                | 24.5 ms: 1.07x faster                                             |
| hexiom                  | 6.34 ms                                                | 5.94 ms: 1.07x faster                                             |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                              |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                             |
| pyflate                 | 419 ms                                                 | 395 ms: 1.06x faster                                              |
| fannkuch                | 384 ms                                                 | 363 ms: 1.06x faster                                              |
| go                      | 140 ms                                                 | 133 ms: 1.06x faster                                              |
| float                   | 76.8 ms                                                | 72.8 ms: 1.05x faster                                             |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                            |
| aiohttp                 | 1.05 ms                                                | 999 us: 1.05x faster                                              |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                              |
| bench_thread_pool       | 817 us                                                 | 779 us: 1.05x faster                                              |
| pprint_safe_repr        | 706 ms                                                 | 674 ms: 1.05x faster                                              |
| deepcopy_reduce         | 3.02 us                                                | 2.88 us: 1.05x faster                                             |
| json                    | 4.87 ms                                                | 4.65 ms: 1.05x faster                                             |
| unpack_sequence         | 44.5 ns                                                | 42.6 ns: 1.04x faster                                             |
| raytrace                | 291 ms                                                 | 280 ms: 1.04x faster                                              |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                            |
| scimark_fft             | 325 ms                                                 | 313 ms: 1.04x faster                                              |
| deepcopy                | 341 us                                                 | 329 us: 1.04x faster                                              |
| pickle_list             | 4.14 us                                                | 3.99 us: 1.04x faster                                             |
| logging_simple          | 6.02 us                                                | 5.81 us: 1.04x faster                                             |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                             |
| 2to3                    | 259 ms                                                 | 251 ms: 1.04x faster                                              |
| genshi_text             | 21.5 ms                                                | 20.8 ms: 1.03x faster                                             |
| sqlglot_optimize        | 52.7 ms                                                | 51.1 ms: 1.03x faster                                             |
| regex_v8                | 22.2 ms                                                | 21.5 ms: 1.03x faster                                             |
| scimark_monte_carlo     | 68.0 ms                                                | 65.9 ms: 1.03x faster                                             |
| crypto_pyaes            | 75.7 ms                                                | 73.7 ms: 1.03x faster                                             |
| deepcopy_memo           | 35.8 us                                                | 34.9 us: 1.03x faster                                             |
| pathlib                 | 18.1 ms                                                | 17.6 ms: 1.03x faster                                             |
| tornado_http            | 96.5 ms                                                | 94.3 ms: 1.02x faster                                             |
| scimark_lu              | 108 ms                                                 | 105 ms: 1.02x faster                                              |
| coverage                | 99.3 ms                                                | 97.1 ms: 1.02x faster                                             |
| async_generators        | 356 ms                                                 | 348 ms: 1.02x faster                                              |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                              |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.02x faster                                             |
| pickle_dict             | 31.2 us                                                | 30.6 us: 1.02x faster                                             |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                              |
| logging_format          | 6.48 us                                                | 6.37 us: 1.02x faster                                             |
| thrift                  | 760 us                                                 | 751 us: 1.01x faster                                              |
| dulwich_log             | 64.0 ms                                                | 63.3 ms: 1.01x faster                                             |
| mako                    | 9.83 ms                                                | 9.73 ms: 1.01x faster                                             |
| telco                   | 6.43 ms                                                | 6.36 ms: 1.01x faster                                             |
| spectral_norm           | 98.1 ms                                                | 97.2 ms: 1.01x faster                                             |
| mdp                     | 2.63 sec                                               | 2.60 sec: 1.01x faster                                            |
| xml_etree_process       | 53.7 ms                                                | 53.3 ms: 1.01x faster                                             |
| django_template         | 32.3 ms                                                | 32.1 ms: 1.01x faster                                             |
| meteor_contest          | 104 ms                                                 | 104 ms: 1.00x faster                                              |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                             |
| pidigits                | 197 ms                                                 | 198 ms: 1.00x slower                                              |
| chameleon               | 6.38 ms                                                | 6.42 ms: 1.01x slower                                             |
| unpickle_list           | 4.99 us                                                | 5.03 us: 1.01x slower                                             |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                            |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                             |
| xml_etree_generate      | 75.9 ms                                                | 77.2 ms: 1.02x slower                                             |
| generators              | 73.5 ms                                                | 74.9 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed | 736 ms                                                 | 754 ms: 1.03x slower                                              |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                             |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                             |
| gc_traversal            | 3.82 ms                                                | 3.96 ms: 1.04x slower                                             |
| python_startup          | 8.58 ms                                                | 8.95 ms: 1.04x slower                                             |
| regex_dna               | 203 ms                                                 | 213 ms: 1.05x slower                                              |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.05x slower                                             |
| regex_effbot            | 3.46 ms                                                | 3.62 ms: 1.05x slower                                             |
| nbody                   | 90.0 ms                                                | 94.5 ms: 1.05x slower                                             |
| async_tree_memoization  | 624 ms                                                 | 664 ms: 1.06x slower                                              |
| python_startup_no_site  | 6.04 ms                                                | 6.48 ms: 1.07x slower                                             |
| dask                    | 365 ms                                                 | 498 ms: 1.36x slower                                              |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (3): unpickle, async_tree_none, djangocms
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230201-3.12.0a4+-2b105e8/bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8.json: mypy
