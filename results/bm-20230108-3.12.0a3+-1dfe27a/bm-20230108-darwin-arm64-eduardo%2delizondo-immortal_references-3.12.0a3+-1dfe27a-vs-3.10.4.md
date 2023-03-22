
# Results vs. 3.10.4

- fork: eduardo-elizondo
- ref: immortal_references
- machine: darwin-arm64
- commit hash: 1dfe27a
- commit date: 2023-01-08
- overall geometric mean: 1.25x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 178 ms: 1.13x faster                                                              |
| chameleon      | 5.79 ms                                                | 4.51 ms: 1.29x faster                                                             |
| docutils       | 1.78 sec                                               | 1.45 sec: 1.23x faster                                                            |
| html5lib       | 44.2 ms                                                | 33.6 ms: 1.32x faster                                                             |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 66.3 ms: 1.41x faster                                                             |
| float          | 72.4 ms                                                | 52.0 ms: 1.39x faster                                                             |
| Geometric mean | (ref)                                                  | 1.25x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 69.8 ms: 1.38x faster                                                             |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                                             |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                              |
| regex_effbot   | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                             |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 187 us: 1.52x faster                                                              |
| unpickle_pure_python | 203 us                                                 | 143 us: 1.43x faster                                                              |
| json_dumps           | 8.40 ms                                                | 5.95 ms: 1.41x faster                                                             |
| xml_etree_process    | 44.8 ms                                                | 35.0 ms: 1.28x faster                                                             |
| xml_etree_parse      | 106 ms                                                 | 94.7 ms: 1.12x faster                                                             |
| xml_etree_generate   | 54.2 ms                                                | 49.3 ms: 1.10x faster                                                             |
| xml_etree_iterparse  | 72.3 ms                                                | 66.3 ms: 1.09x faster                                                             |
| json_loads           | 16.9 us                                                | 16.3 us: 1.03x faster                                                             |
| unpickle_list        | 2.69 us                                                | 2.66 us: 1.01x faster                                                             |
| pickle_dict          | 17.9 us                                                | 18.1 us: 1.01x slower                                                             |
| pickle_list          | 2.80 us                                                | 2.86 us: 1.02x slower                                                             |
| unpickle             | 9.89 us                                                | 10.2 us: 1.03x slower                                                             |
| pickle               | 7.35 us                                                | 7.69 us: 1.05x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.33 ms: 1.28x faster                                                             |
| python_startup_no_site | 8.88 ms                                                | 7.31 ms: 1.21x faster                                                             |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 27.3 ms                                                | 20.9 ms: 1.30x faster                                                             |
| genshi_xml      | 37.2 ms                                                | 28.5 ms: 1.30x faster                                                             |
| genshi_text     | 18.4 ms                                                | 14.4 ms: 1.28x faster                                                             |
| mako            | 10.5 ms                                                | 8.51 ms: 1.23x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.56 ms: 2.01x faster                                                             |
| logging_silent          | 119 ns                                                 | 63.7 ns: 1.88x faster                                                             |
| richards                | 51.4 ms                                                | 28.9 ms: 1.78x faster                                                             |
| asyncio_tcp             | 670 ms                                                 | 412 ms: 1.62x faster                                                              |
| go                      | 165 ms                                                 | 103 ms: 1.61x faster                                                              |
| scimark_monte_carlo     | 72.5 ms                                                | 46.2 ms: 1.57x faster                                                             |
| async_tree_memoization  | 490 ms                                                 | 317 ms: 1.54x faster                                                              |
| pickle_pure_python      | 283 us                                                 | 187 us: 1.52x faster                                                              |
| crypto_pyaes            | 78.1 ms                                                | 52.0 ms: 1.50x faster                                                             |
| scimark_sor             | 126 ms                                                 | 84.0 ms: 1.50x faster                                                             |
| raytrace                | 325 ms                                                 | 222 ms: 1.46x faster                                                              |
| async_tree_none         | 400 ms                                                 | 276 ms: 1.45x faster                                                              |
| chaos                   | 66.7 ms                                                | 46.1 ms: 1.45x faster                                                             |
| scimark_lu              | 109 ms                                                 | 75.7 ms: 1.44x faster                                                             |
| unpickle_pure_python    | 203 us                                                 | 143 us: 1.43x faster                                                              |
| hexiom                  | 6.32 ms                                                | 4.44 ms: 1.42x faster                                                             |
| pyflate                 | 453 ms                                                 | 319 ms: 1.42x faster                                                              |
| async_tree_io           | 1.02 sec                                               | 720 ms: 1.42x faster                                                              |
| json_dumps              | 8.40 ms                                                | 5.95 ms: 1.41x faster                                                             |
| nbody                   | 93.3 ms                                                | 66.3 ms: 1.41x faster                                                             |
| logging_simple          | 4.63 us                                                | 3.30 us: 1.40x faster                                                             |
| float                   | 72.4 ms                                                | 52.0 ms: 1.39x faster                                                             |
| logging_format          | 4.97 us                                                | 3.59 us: 1.38x faster                                                             |
| pathlib                 | 28.8 ms                                                | 20.8 ms: 1.38x faster                                                             |
| regex_compile           | 96.4 ms                                                | 69.8 ms: 1.38x faster                                                             |
| sqlglot_parse           | 1.37 ms                                                | 991 us: 1.38x faster                                                              |
| pycparser               | 916 ms                                                 | 667 ms: 1.37x faster                                                              |
| sqlglot_transpile       | 1.57 ms                                                | 1.15 ms: 1.37x faster                                                             |
| fannkuch                | 317 ms                                                 | 232 ms: 1.37x faster                                                              |
| pprint_pformat          | 1.23 sec                                               | 910 ms: 1.35x faster                                                              |
| pprint_safe_repr        | 606 ms                                                 | 448 ms: 1.35x faster                                                              |
| thrift                  | 580 us                                                 | 431 us: 1.35x faster                                                              |
| deepcopy_memo           | 34.4 us                                                | 25.6 us: 1.34x faster                                                             |
| dulwich_log             | 37.1 ms                                                | 27.9 ms: 1.33x faster                                                             |
| html5lib                | 44.2 ms                                                | 33.6 ms: 1.32x faster                                                             |
| spectral_norm           | 95.8 ms                                                | 73.0 ms: 1.31x faster                                                             |
| deepcopy                | 281 us                                                 | 215 us: 1.31x faster                                                              |
| django_template         | 27.3 ms                                                | 20.9 ms: 1.30x faster                                                             |
| genshi_xml              | 37.2 ms                                                | 28.5 ms: 1.30x faster                                                             |
| unpack_sequence         | 37.4 ns                                                | 28.8 ns: 1.30x faster                                                             |
| create_gc_cycles        | 880 us                                                 | 677 us: 1.30x faster                                                              |
| chameleon               | 5.79 ms                                                | 4.51 ms: 1.29x faster                                                             |
| deepcopy_reduce         | 2.37 us                                                | 1.85 us: 1.28x faster                                                             |
| xml_etree_process       | 44.8 ms                                                | 35.0 ms: 1.28x faster                                                             |
| genshi_text             | 18.4 ms                                                | 14.4 ms: 1.28x faster                                                             |
| python_startup          | 11.9 ms                                                | 9.33 ms: 1.28x faster                                                             |
| async_tree_cpu_io_mixed | 669 ms                                                 | 530 ms: 1.26x faster                                                              |
| mako                    | 10.5 ms                                                | 8.51 ms: 1.23x faster                                                             |
| bench_thread_pool       | 546 us                                                 | 443 us: 1.23x faster                                                              |
| docutils                | 1.78 sec                                               | 1.45 sec: 1.23x faster                                                            |
| sqlglot_optimize        | 38.0 ms                                                | 31.1 ms: 1.22x faster                                                             |
| nqueens                 | 68.2 ms                                                | 55.9 ms: 1.22x faster                                                             |
| python_startup_no_site  | 8.88 ms                                                | 7.31 ms: 1.21x faster                                                             |
| coroutines              | 20.2 ms                                                | 16.8 ms: 1.20x faster                                                             |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.90 ms: 1.19x faster                                                             |
| sympy_expand            | 275 ms                                                 | 232 ms: 1.19x faster                                                              |
| async_generators        | 234 ms                                                 | 197 ms: 1.19x faster                                                              |
| sympy_integrate         | 13.3 ms                                                | 11.2 ms: 1.18x faster                                                             |
| sympy_str               | 169 ms                                                 | 145 ms: 1.17x faster                                                              |
| scimark_fft             | 230 ms                                                 | 199 ms: 1.16x faster                                                              |
| sqlglot_normalize       | 196 ms                                                 | 170 ms: 1.15x faster                                                              |
| 2to3                    | 201 ms                                                 | 178 ms: 1.13x faster                                                              |
| sympy_sum               | 93.6 ms                                                | 83.2 ms: 1.13x faster                                                             |
| xml_etree_parse         | 106 ms                                                 | 94.7 ms: 1.12x faster                                                             |
| mdp                     | 1.66 sec                                               | 1.50 sec: 1.11x faster                                                            |
| xml_etree_generate      | 54.2 ms                                                | 49.3 ms: 1.10x faster                                                             |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                                             |
| xml_etree_iterparse     | 72.3 ms                                                | 66.3 ms: 1.09x faster                                                             |
| json                    | 3.08 ms                                                | 2.83 ms: 1.09x faster                                                             |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                              |
| sqlite_synth            | 1.47 us                                                | 1.40 us: 1.05x faster                                                             |
| telco                   | 3.63 ms                                                | 3.45 ms: 1.05x faster                                                             |
| meteor_contest          | 78.1 ms                                                | 74.3 ms: 1.05x faster                                                             |
| json_loads              | 16.9 us                                                | 16.3 us: 1.03x faster                                                             |
| unpickle_list           | 2.69 us                                                | 2.66 us: 1.01x faster                                                             |
| gc_traversal            | 2.39 ms                                                | 2.40 ms: 1.00x slower                                                             |
| pickle_dict             | 17.9 us                                                | 18.1 us: 1.01x slower                                                             |
| pickle_list             | 2.80 us                                                | 2.86 us: 1.02x slower                                                             |
| generators              | 32.7 ms                                                | 33.7 ms: 1.03x slower                                                             |
| unpickle                | 9.89 us                                                | 10.2 us: 1.03x slower                                                             |
| pickle                  | 7.35 us                                                | 7.69 us: 1.05x slower                                                             |
| regex_effbot            | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                             |
| bench_mp_pool           | 39.7 ms                                                | 42.9 ms: 1.08x slower                                                             |
| dask                    | 265 ms                                                 | 315 ms: 1.19x slower                                                              |
| coverage                | 42.0 ms                                                | 56.2 ms: 1.34x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.25x faster                                                                      |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (9) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, comprehensions, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230108-3.12.0a3+-1dfe27a/bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a.json: mypy
