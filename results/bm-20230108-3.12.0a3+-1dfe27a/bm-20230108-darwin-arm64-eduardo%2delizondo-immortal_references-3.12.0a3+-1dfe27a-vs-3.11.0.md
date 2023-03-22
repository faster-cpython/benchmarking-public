
# Results vs. 3.11.0

- fork: eduardo-elizondo
- ref: immortal_references
- machine: darwin-arm64
- commit hash: 1dfe27a
- commit date: 2023-01-08
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 178 ms: 1.11x slower                                                              |
| chameleon      | 4.57 ms                                                | 4.51 ms: 1.01x faster                                                             |
| docutils       | 1.47 sec                                               | 1.45 sec: 1.02x faster                                                            |
| html5lib       | 34.7 ms                                                | 33.6 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 52.0 ms: 1.02x faster                                                             |
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                                              |
| nbody          | 65.5 ms                                                | 66.3 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 69.8 ms: 1.10x faster                                                             |
| regex_dna      | 152 ms                                                 | 149 ms: 1.01x faster                                                              |
| regex_v8       | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 5.95 ms: 1.30x faster                                                             |
| xml_etree_parse      | 106 ms                                                 | 94.7 ms: 1.12x faster                                                             |
| unpickle_pure_python | 159 us                                                 | 143 us: 1.11x faster                                                              |
| pickle_pure_python   | 199 us                                                 | 187 us: 1.06x faster                                                              |
| xml_etree_iterparse  | 69.2 ms                                                | 66.3 ms: 1.04x faster                                                             |
| xml_etree_process    | 35.2 ms                                                | 35.0 ms: 1.01x faster                                                             |
| xml_etree_generate   | 48.8 ms                                                | 49.3 ms: 1.01x slower                                                             |
| unpickle_list        | 2.63 us                                                | 2.66 us: 1.01x slower                                                             |
| pickle_dict          | 17.9 us                                                | 18.1 us: 1.01x slower                                                             |
| json_loads           | 16.1 us                                                | 16.3 us: 1.02x slower                                                             |
| pickle_list          | 2.81 us                                                | 2.86 us: 1.02x slower                                                             |
| unpickle             | 9.70 us                                                | 10.2 us: 1.05x slower                                                             |
| pickle               | 7.17 us                                                | 7.69 us: 1.07x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.31 ms: 1.27x faster                                                             |
| python_startup         | 11.5 ms                                                | 9.33 ms: 1.24x faster                                                             |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 15.3 ms                                                | 14.4 ms: 1.06x faster                                                             |
| genshi_xml      | 29.8 ms                                                | 28.5 ms: 1.04x faster                                                             |
| django_template | 21.0 ms                                                | 20.9 ms: 1.01x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 412 ms: 1.58x faster                                                              |
| pathlib                 | 27.8 ms                                                | 20.8 ms: 1.33x faster                                                             |
| json_dumps              | 7.72 ms                                                | 5.95 ms: 1.30x faster                                                             |
| python_startup_no_site  | 9.31 ms                                                | 7.31 ms: 1.27x faster                                                             |
| python_startup          | 11.5 ms                                                | 9.33 ms: 1.24x faster                                                             |
| unpack_sequence         | 33.6 ns                                                | 28.8 ns: 1.17x faster                                                             |
| fannkuch                | 261 ms                                                 | 232 ms: 1.12x faster                                                              |
| xml_etree_parse         | 106 ms                                                 | 94.7 ms: 1.12x faster                                                             |
| unpickle_pure_python    | 159 us                                                 | 143 us: 1.11x faster                                                              |
| richards                | 32.2 ms                                                | 28.9 ms: 1.11x faster                                                             |
| nqueens                 | 61.8 ms                                                | 55.9 ms: 1.11x faster                                                             |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.90 ms: 1.11x faster                                                             |
| deltablue               | 2.81 ms                                                | 2.56 ms: 1.10x faster                                                             |
| regex_compile           | 76.7 ms                                                | 69.8 ms: 1.10x faster                                                             |
| chaos                   | 49.5 ms                                                | 46.1 ms: 1.07x faster                                                             |
| create_gc_cycles        | 726 us                                                 | 677 us: 1.07x faster                                                              |
| dulwich_log             | 29.9 ms                                                | 27.9 ms: 1.07x faster                                                             |
| logging_silent          | 68.0 ns                                                | 63.7 ns: 1.07x faster                                                             |
| bench_thread_pool       | 473 us                                                 | 443 us: 1.07x faster                                                              |
| hexiom                  | 4.73 ms                                                | 4.44 ms: 1.07x faster                                                             |
| pickle_pure_python      | 199 us                                                 | 187 us: 1.06x faster                                                              |
| genshi_text             | 15.3 ms                                                | 14.4 ms: 1.06x faster                                                             |
| logging_simple          | 3.50 us                                                | 3.30 us: 1.06x faster                                                             |
| go                      | 109 ms                                                 | 103 ms: 1.06x faster                                                              |
| async_tree_memoization  | 336 ms                                                 | 317 ms: 1.06x faster                                                              |
| coroutines              | 17.7 ms                                                | 16.8 ms: 1.06x faster                                                             |
| logging_format          | 3.78 us                                                | 3.59 us: 1.05x faster                                                             |
| sympy_expand            | 243 ms                                                 | 232 ms: 1.05x faster                                                              |
| sympy_str               | 152 ms                                                 | 145 ms: 1.05x faster                                                              |
| genshi_xml              | 29.8 ms                                                | 28.5 ms: 1.04x faster                                                             |
| pprint_pformat          | 950 ms                                                 | 910 ms: 1.04x faster                                                              |
| pycparser               | 697 ms                                                 | 667 ms: 1.04x faster                                                              |
| xml_etree_iterparse     | 69.2 ms                                                | 66.3 ms: 1.04x faster                                                             |
| coverage                | 58.6 ms                                                | 56.2 ms: 1.04x faster                                                             |
| deepcopy                | 224 us                                                 | 215 us: 1.04x faster                                                              |
| pprint_safe_repr        | 465 ms                                                 | 448 ms: 1.04x faster                                                              |
| sympy_sum               | 86.0 ms                                                | 83.2 ms: 1.03x faster                                                             |
| html5lib                | 34.7 ms                                                | 33.6 ms: 1.03x faster                                                             |
| deepcopy_reduce         | 1.91 us                                                | 1.85 us: 1.03x faster                                                             |
| async_tree_none         | 285 ms                                                 | 276 ms: 1.03x faster                                                              |
| mdp                     | 1.54 sec                                               | 1.50 sec: 1.03x faster                                                            |
| deepcopy_memo           | 26.3 us                                                | 25.6 us: 1.03x faster                                                             |
| sympy_integrate         | 11.5 ms                                                | 11.2 ms: 1.02x faster                                                             |
| float                   | 53.0 ms                                                | 52.0 ms: 1.02x faster                                                             |
| docutils                | 1.47 sec                                               | 1.45 sec: 1.02x faster                                                            |
| regex_dna               | 152 ms                                                 | 149 ms: 1.01x faster                                                              |
| chameleon               | 4.57 ms                                                | 4.51 ms: 1.01x faster                                                             |
| gc_traversal            | 2.43 ms                                                | 2.40 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed | 534 ms                                                 | 530 ms: 1.01x faster                                                              |
| xml_etree_process       | 35.2 ms                                                | 35.0 ms: 1.01x faster                                                             |
| regex_v8                | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                             |
| django_template         | 21.0 ms                                                | 20.9 ms: 1.01x faster                                                             |
| sqlglot_normalize       | 171 ms                                                 | 170 ms: 1.01x faster                                                              |
| thrift                  | 433 us                                                 | 431 us: 1.00x faster                                                              |
| scimark_monte_carlo     | 46.4 ms                                                | 46.2 ms: 1.00x faster                                                             |
| sqlglot_optimize        | 31.2 ms                                                | 31.1 ms: 1.00x faster                                                             |
| scimark_fft             | 199 ms                                                 | 199 ms: 1.00x faster                                                              |
| spectral_norm           | 72.8 ms                                                | 73.0 ms: 1.00x slower                                                             |
| crypto_pyaes            | 51.7 ms                                                | 52.0 ms: 1.01x slower                                                             |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                                              |
| meteor_contest          | 73.8 ms                                                | 74.3 ms: 1.01x slower                                                             |
| xml_etree_generate      | 48.8 ms                                                | 49.3 ms: 1.01x slower                                                             |
| unpickle_list           | 2.63 us                                                | 2.66 us: 1.01x slower                                                             |
| async_generators        | 195 ms                                                 | 197 ms: 1.01x slower                                                              |
| nbody                   | 65.5 ms                                                | 66.3 ms: 1.01x slower                                                             |
| scimark_sor             | 83.0 ms                                                | 84.0 ms: 1.01x slower                                                             |
| pickle_dict             | 17.9 us                                                | 18.1 us: 1.01x slower                                                             |
| telco                   | 3.39 ms                                                | 3.45 ms: 1.02x slower                                                             |
| json_loads              | 16.1 us                                                | 16.3 us: 1.02x slower                                                             |
| async_tree_io           | 706 ms                                                 | 720 ms: 1.02x slower                                                              |
| pickle_list             | 2.81 us                                                | 2.86 us: 1.02x slower                                                             |
| json                    | 2.77 ms                                                | 2.83 ms: 1.02x slower                                                             |
| pyflate                 | 311 ms                                                 | 319 ms: 1.03x slower                                                              |
| sqlglot_transpile       | 1.12 ms                                                | 1.15 ms: 1.03x slower                                                             |
| sqlglot_parse           | 957 us                                                 | 991 us: 1.03x slower                                                              |
| unpickle                | 9.70 us                                                | 10.2 us: 1.05x slower                                                             |
| scimark_lu              | 72.1 ms                                                | 75.7 ms: 1.05x slower                                                             |
| pickle                  | 7.17 us                                                | 7.69 us: 1.07x slower                                                             |
| raytrace                | 207 ms                                                 | 222 ms: 1.07x slower                                                              |
| sqlite_synth            | 1.27 us                                                | 1.40 us: 1.10x slower                                                             |
| 2to3                    | 161 ms                                                 | 178 ms: 1.11x slower                                                              |
| generators              | 28.8 ms                                                | 33.7 ms: 1.17x slower                                                             |
| dask                    | 226 ms                                                 | 315 ms: 1.39x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (3): bench_mp_pool, regex_effbot, mako
Ignored benchmarks (9) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, comprehensions, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230108-3.12.0a3+-1dfe27a/bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a.json: mypy
