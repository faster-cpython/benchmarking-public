
# Results vs. 3.11.0

- fork: eduardo-elizondo
- ref: immortal_references
- machine: linux-x86_64
- commit hash: 1dfe27a
- commit date: 2023-01-08
- overall geometric mean: 1.03x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 274 ms: 1.06x slower                                                              |
| chameleon      | 6.38 ms                                                | 6.83 ms: 1.07x slower                                                             |
| docutils       | 2.60 sec                                               | 2.69 sec: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                                              |
| float          | 76.8 ms                                                | 79.7 ms: 1.04x slower                                                             |
| nbody          | 90.0 ms                                                | 96.7 ms: 1.07x slower                                                             |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.1 ms: 1.06x faster                                                             |
| regex_effbot   | 3.46 ms                                                | 3.39 ms: 1.02x faster                                                             |
| regex_dna      | 203 ms                                                 | 203 ms: 1.00x faster                                                              |
| regex_compile  | 136 ms                                                 | 144 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.78 ms: 1.26x faster                                                             |
| xml_etree_parse      | 160 ms                                                 | 151 ms: 1.06x faster                                                              |
| unpickle_pure_python | 227 us                                                 | 217 us: 1.04x faster                                                              |
| unpickle_list        | 4.99 us                                                | 4.79 us: 1.04x faster                                                             |
| pickle_dict          | 31.2 us                                                | 30.5 us: 1.02x faster                                                             |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                              |
| json_loads           | 26.1 us                                                | 26.6 us: 1.02x slower                                                             |
| unpickle             | 13.3 us                                                | 13.7 us: 1.03x slower                                                             |
| xml_etree_generate   | 75.9 ms                                                | 79.5 ms: 1.05x slower                                                             |
| pickle_list          | 4.14 us                                                | 4.35 us: 1.05x slower                                                             |
| xml_etree_process    | 53.7 ms                                                | 56.7 ms: 1.06x slower                                                             |
| pickle               | 9.90 us                                                | 10.5 us: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.77 ms: 1.02x slower                                                             |
| python_startup_no_site | 6.04 ms                                                | 6.21 ms: 1.03x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 51.0 ms: 1.01x faster                                                             |
| genshi_text     | 21.5 ms                                                | 22.2 ms: 1.03x slower                                                             |
| mako            | 9.83 ms                                                | 10.5 ms: 1.07x slower                                                             |
| django_template | 32.3 ms                                                | 34.8 ms: 1.08x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 514 ms: 1.72x faster                                                              |
| json_dumps              | 12.4 ms                                                | 9.78 ms: 1.26x faster                                                             |
| xml_etree_parse         | 160 ms                                                 | 151 ms: 1.06x faster                                                              |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.34 ms: 1.06x faster                                                             |
| regex_v8                | 22.2 ms                                                | 21.1 ms: 1.06x faster                                                             |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                              |
| nqueens                 | 83.8 ms                                                | 80.1 ms: 1.05x faster                                                             |
| unpickle_pure_python    | 227 us                                                 | 217 us: 1.04x faster                                                              |
| unpickle_list           | 4.99 us                                                | 4.79 us: 1.04x faster                                                             |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                                              |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.04x faster                                                             |
| pycparser               | 1.19 sec                                               | 1.15 sec: 1.03x faster                                                            |
| richards                | 46.1 ms                                                | 44.9 ms: 1.03x faster                                                             |
| pickle_dict             | 31.2 us                                                | 30.5 us: 1.02x faster                                                             |
| regex_effbot            | 3.46 ms                                                | 3.39 ms: 1.02x faster                                                             |
| genshi_xml              | 51.4 ms                                                | 51.0 ms: 1.01x faster                                                             |
| mdp                     | 2.63 sec                                               | 2.61 sec: 1.01x faster                                                            |
| regex_dna               | 203 ms                                                 | 203 ms: 1.00x faster                                                              |
| fannkuch                | 384 ms                                                 | 387 ms: 1.01x slower                                                              |
| hexiom                  | 6.34 ms                                                | 6.38 ms: 1.01x slower                                                             |
| chaos                   | 68.7 ms                                                | 69.2 ms: 1.01x slower                                                             |
| deltablue               | 3.66 ms                                                | 3.68 ms: 1.01x slower                                                             |
| coroutines              | 26.2 ms                                                | 26.6 ms: 1.02x slower                                                             |
| pathlib                 | 18.1 ms                                                | 18.4 ms: 1.02x slower                                                             |
| async_tree_none         | 526 ms                                                 | 536 ms: 1.02x slower                                                              |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                                              |
| pprint_pformat          | 1.46 sec                                               | 1.49 sec: 1.02x slower                                                            |
| thrift                  | 760 us                                                 | 775 us: 1.02x slower                                                              |
| bench_thread_pool       | 817 us                                                 | 834 us: 1.02x slower                                                              |
| json_loads              | 26.1 us                                                | 26.6 us: 1.02x slower                                                             |
| python_startup          | 8.58 ms                                                | 8.77 ms: 1.02x slower                                                             |
| gc_traversal            | 3.82 ms                                                | 3.90 ms: 1.02x slower                                                             |
| scimark_monte_carlo     | 68.0 ms                                                | 69.6 ms: 1.02x slower                                                             |
| pyflate                 | 419 ms                                                 | 429 ms: 1.02x slower                                                              |
| json                    | 4.87 ms                                                | 5.00 ms: 1.03x slower                                                             |
| async_tree_io           | 1.30 sec                                               | 1.34 sec: 1.03x slower                                                            |
| python_startup_no_site  | 6.04 ms                                                | 6.21 ms: 1.03x slower                                                             |
| logging_silent          | 98.0 ns                                                | 101 ns: 1.03x slower                                                              |
| coverage                | 99.3 ms                                                | 102 ms: 1.03x slower                                                              |
| genshi_text             | 21.5 ms                                                | 22.2 ms: 1.03x slower                                                             |
| telco                   | 6.43 ms                                                | 6.64 ms: 1.03x slower                                                             |
| djangocms               | 32.5 us                                                | 33.6 us: 1.03x slower                                                             |
| pprint_safe_repr        | 706 ms                                                 | 729 ms: 1.03x slower                                                              |
| unpickle                | 13.3 us                                                | 13.7 us: 1.03x slower                                                             |
| docutils                | 2.60 sec                                               | 2.69 sec: 1.03x slower                                                            |
| float                   | 76.8 ms                                                | 79.7 ms: 1.04x slower                                                             |
| async_tree_cpu_io_mixed | 736 ms                                                 | 765 ms: 1.04x slower                                                              |
| crypto_pyaes            | 75.7 ms                                                | 79.0 ms: 1.04x slower                                                             |
| sqlglot_optimize        | 52.7 ms                                                | 55.2 ms: 1.05x slower                                                             |
| xml_etree_generate      | 75.9 ms                                                | 79.5 ms: 1.05x slower                                                             |
| logging_simple          | 6.02 us                                                | 6.31 us: 1.05x slower                                                             |
| pickle_list             | 4.14 us                                                | 4.35 us: 1.05x slower                                                             |
| scimark_sor             | 115 ms                                                 | 121 ms: 1.05x slower                                                              |
| sympy_integrate         | 21.0 ms                                                | 22.0 ms: 1.05x slower                                                             |
| sympy_expand            | 475 ms                                                 | 501 ms: 1.05x slower                                                              |
| async_generators        | 356 ms                                                 | 375 ms: 1.05x slower                                                              |
| 2to3                    | 259 ms                                                 | 274 ms: 1.06x slower                                                              |
| xml_etree_process       | 53.7 ms                                                | 56.7 ms: 1.06x slower                                                             |
| sqlglot_normalize       | 108 ms                                                 | 114 ms: 1.06x slower                                                              |
| regex_compile           | 136 ms                                                 | 144 ms: 1.06x slower                                                              |
| deepcopy_memo           | 35.8 us                                                | 38.0 us: 1.06x slower                                                             |
| raytrace                | 291 ms                                                 | 309 ms: 1.06x slower                                                              |
| pickle                  | 9.90 us                                                | 10.5 us: 1.06x slower                                                             |
| deepcopy_reduce         | 3.02 us                                                | 3.21 us: 1.07x slower                                                             |
| mako                    | 9.83 ms                                                | 10.5 ms: 1.07x slower                                                             |
| sqlite_synth            | 2.48 us                                                | 2.65 us: 1.07x slower                                                             |
| scimark_lu              | 108 ms                                                 | 115 ms: 1.07x slower                                                              |
| sympy_str               | 291 ms                                                 | 311 ms: 1.07x slower                                                              |
| deepcopy                | 341 us                                                 | 366 us: 1.07x slower                                                              |
| chameleon               | 6.38 ms                                                | 6.83 ms: 1.07x slower                                                             |
| dulwich_log             | 64.0 ms                                                | 68.7 ms: 1.07x slower                                                             |
| nbody                   | 90.0 ms                                                | 96.7 ms: 1.07x slower                                                             |
| logging_format          | 6.48 us                                                | 6.96 us: 1.07x slower                                                             |
| django_template         | 32.3 ms                                                | 34.8 ms: 1.08x slower                                                             |
| spectral_norm           | 98.1 ms                                                | 106 ms: 1.08x slower                                                              |
| generators              | 73.5 ms                                                | 80.5 ms: 1.10x slower                                                             |
| sympy_sum               | 166 ms                                                 | 182 ms: 1.10x slower                                                              |
| async_tree_memoization  | 624 ms                                                 | 688 ms: 1.10x slower                                                              |
| scimark_fft             | 325 ms                                                 | 359 ms: 1.10x slower                                                              |
| meteor_contest          | 104 ms                                                 | 116 ms: 1.11x slower                                                              |
| sqlglot_transpile       | 1.65 ms                                                | 1.87 ms: 1.13x slower                                                             |
| sqlglot_parse           | 1.36 ms                                                | 1.55 ms: 1.14x slower                                                             |
| unpack_sequence         | 44.5 ns                                                | 51.6 ns: 1.16x slower                                                             |
| dask                    | 365 ms                                                 | 545 ms: 1.49x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.03x slower                                                                      |

Benchmark hidden because not significant (3): html5lib, bench_mp_pool, pickle_pure_python
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230108-3.12.0a3+-1dfe27a/bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a.json: mypy
