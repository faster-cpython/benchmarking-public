
# Results vs. 3.10.4

- fork: eduardo-elizondo
- ref: immortal_references
- machine: windows-amd64
- commit hash: 9423c61
- commit date: 2023-04-20
- overall geometric mean: 1.19x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 204 ms: 1.16x faster                                                                   |
| chameleon      | 5.92 ms                                                     | 4.88 ms: 1.21x faster                                                                  |
| docutils       | 1.89 sec                                                    | 1.56 sec: 1.22x faster                                                                 |
| html5lib       | 46.5 ms                                                     | 36.4 ms: 1.28x faster                                                                  |
| tornado_http   | 109 ms                                                      | 88.8 ms: 1.23x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 50.9 ms: 1.18x faster                                                                  |
| nbody          | 69.3 ms                                                     | 68.3 ms: 1.02x faster                                                                  |
| pidigits       | 145 ms                                                      | 148 ms: 1.02x slower                                                                   |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 82.1 ms: 1.26x faster                                                                  |
| regex_dna      | 132 ms                                                      | 123 ms: 1.07x faster                                                                   |
| regex_v8       | 15.0 ms                                                     | 14.1 ms: 1.07x faster                                                                  |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.36 ms: 1.59x faster                                                                  |
| pickle_pure_python   | 257 us                                                      | 188 us: 1.36x faster                                                                   |
| unpickle_pure_python | 171 us                                                      | 132 us: 1.30x faster                                                                   |
| xml_etree_process    | 43.4 ms                                                     | 36.2 ms: 1.20x faster                                                                  |
| xml_etree_parse      | 102 ms                                                      | 88.1 ms: 1.16x faster                                                                  |
| unpickle             | 9.17 us                                                     | 8.18 us: 1.12x faster                                                                  |
| json_loads           | 14.2 us                                                     | 13.0 us: 1.09x faster                                                                  |
| xml_etree_iterparse  | 63.5 ms                                                     | 60.0 ms: 1.06x faster                                                                  |
| xml_etree_generate   | 54.5 ms                                                     | 52.4 ms: 1.04x faster                                                                  |
| unpickle_list        | 2.81 us                                                     | 2.71 us: 1.04x faster                                                                  |
| pickle_dict          | 16.9 us                                                     | 18.3 us: 1.08x slower                                                                  |
| pickle_list          | 2.59 us                                                     | 2.80 us: 1.08x slower                                                                  |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.62 ms: 1.33x faster                                                                  |
| django_template | 28.2 ms                                                     | 21.7 ms: 1.30x faster                                                                  |
| genshi_text     | 19.0 ms                                                     | 14.9 ms: 1.28x faster                                                                  |
| genshi_xml      | 40.5 ms                                                     | 31.9 ms: 1.27x faster                                                                  |
| Geometric mean  | (ref)                                                       | 1.29x faster                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.17 ms: 1.92x faster                                                                  |
| mypy2                   | 352 ms                                                      | 214 ms: 1.64x faster                                                                   |
| logging_silent          | 96.4 ns                                                     | 58.9 ns: 1.64x faster                                                                  |
| json_dumps              | 8.50 ms                                                     | 5.36 ms: 1.59x faster                                                                  |
| go                      | 136 ms                                                      | 86.2 ms: 1.58x faster                                                                  |
| scimark_lu              | 85.4 ms                                                     | 54.3 ms: 1.57x faster                                                                  |
| richards                | 41.2 ms                                                     | 26.5 ms: 1.56x faster                                                                  |
| sqlglot_parse           | 1.22 ms                                                     | 787 us: 1.55x faster                                                                   |
| asyncio_tcp             | 712 ms                                                      | 475 ms: 1.50x faster                                                                   |
| raytrace                | 271 ms                                                      | 182 ms: 1.49x faster                                                                   |
| sqlglot_transpile       | 1.46 ms                                                     | 988 us: 1.48x faster                                                                   |
| generators              | 31.6 ms                                                     | 21.5 ms: 1.47x faster                                                                  |
| async_tree_memoization  | 497 ms                                                      | 350 ms: 1.42x faster                                                                   |
| async_tree_io           | 1.07 sec                                                    | 759 ms: 1.40x faster                                                                   |
| hexiom                  | 5.52 ms                                                     | 3.97 ms: 1.39x faster                                                                  |
| chaos                   | 58.9 ms                                                     | 42.5 ms: 1.39x faster                                                                  |
| async_tree_none         | 420 ms                                                      | 304 ms: 1.38x faster                                                                   |
| pickle_pure_python      | 257 us                                                      | 188 us: 1.36x faster                                                                   |
| crypto_pyaes            | 62.3 ms                                                     | 45.9 ms: 1.36x faster                                                                  |
| pyflate                 | 387 ms                                                      | 288 ms: 1.34x faster                                                                   |
| mako                    | 8.80 ms                                                     | 6.62 ms: 1.33x faster                                                                  |
| scimark_monte_carlo     | 55.9 ms                                                     | 42.1 ms: 1.33x faster                                                                  |
| scimark_sor             | 105 ms                                                      | 79.0 ms: 1.33x faster                                                                  |
| pycparser               | 868 ms                                                      | 659 ms: 1.32x faster                                                                   |
| thrift                  | 615 us                                                      | 473 us: 1.30x faster                                                                   |
| django_template         | 28.2 ms                                                     | 21.7 ms: 1.30x faster                                                                  |
| unpickle_pure_python    | 171 us                                                      | 132 us: 1.30x faster                                                                   |
| async_tree_cpu_io_mixed | 609 ms                                                      | 471 ms: 1.29x faster                                                                   |
| spectral_norm           | 78.0 ms                                                     | 60.5 ms: 1.29x faster                                                                  |
| mdp                     | 1.71 sec                                                    | 1.34 sec: 1.28x faster                                                                 |
| genshi_text             | 19.0 ms                                                     | 14.9 ms: 1.28x faster                                                                  |
| html5lib                | 46.5 ms                                                     | 36.4 ms: 1.28x faster                                                                  |
| genshi_xml              | 40.5 ms                                                     | 31.9 ms: 1.27x faster                                                                  |
| pylint                  | 347 ms                                                      | 274 ms: 1.27x faster                                                                   |
| regex_compile           | 103 ms                                                      | 82.1 ms: 1.26x faster                                                                  |
| deepcopy_memo           | 28.5 us                                                     | 22.9 us: 1.25x faster                                                                  |
| tornado_http            | 109 ms                                                      | 88.8 ms: 1.23x faster                                                                  |
| docutils                | 1.89 sec                                                    | 1.56 sec: 1.22x faster                                                                 |
| pprint_safe_repr        | 589 ms                                                      | 484 ms: 1.22x faster                                                                   |
| chameleon               | 5.92 ms                                                     | 4.88 ms: 1.21x faster                                                                  |
| sqlglot_optimize        | 39.0 ms                                                     | 32.2 ms: 1.21x faster                                                                  |
| pprint_pformat          | 1.21 sec                                                    | 999 ms: 1.21x faster                                                                   |
| xml_etree_process       | 43.4 ms                                                     | 36.2 ms: 1.20x faster                                                                  |
| coroutines              | 15.9 ms                                                     | 13.4 ms: 1.19x faster                                                                  |
| float                   | 60.2 ms                                                     | 50.9 ms: 1.18x faster                                                                  |
| bench_thread_pool       | 946 us                                                      | 809 us: 1.17x faster                                                                   |
| dulwich_log             | 47.6 ms                                                     | 40.9 ms: 1.16x faster                                                                  |
| 2to3                    | 237 ms                                                      | 204 ms: 1.16x faster                                                                   |
| nqueens                 | 67.0 ms                                                     | 57.8 ms: 1.16x faster                                                                  |
| xml_etree_parse         | 102 ms                                                      | 88.1 ms: 1.16x faster                                                                  |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.31 ms: 1.15x faster                                                                  |
| sympy_expand            | 315 ms                                                      | 274 ms: 1.15x faster                                                                   |
| sqlglot_normalize       | 202 ms                                                      | 176 ms: 1.15x faster                                                                   |
| create_gc_cycles        | 782 us                                                      | 686 us: 1.14x faster                                                                   |
| scimark_fft             | 193 ms                                                      | 170 ms: 1.14x faster                                                                   |
| sympy_integrate         | 14.8 ms                                                     | 13.1 ms: 1.13x faster                                                                  |
| unpickle                | 9.17 us                                                     | 8.18 us: 1.12x faster                                                                  |
| deepcopy                | 255 us                                                      | 228 us: 1.12x faster                                                                   |
| json                    | 3.05 ms                                                     | 2.74 ms: 1.11x faster                                                                  |
| sympy_str               | 188 ms                                                      | 171 ms: 1.10x faster                                                                   |
| deepcopy_reduce         | 2.16 us                                                     | 1.96 us: 1.10x faster                                                                  |
| sympy_sum               | 104 ms                                                      | 94.7 ms: 1.10x faster                                                                  |
| python_startup          | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                                  |
| json_loads              | 14.2 us                                                     | 13.0 us: 1.09x faster                                                                  |
| comprehensions          | 16.0 us                                                     | 14.8 us: 1.08x faster                                                                  |
| regex_dna               | 132 ms                                                      | 123 ms: 1.07x faster                                                                   |
| regex_v8                | 15.0 ms                                                     | 14.1 ms: 1.07x faster                                                                  |
| xml_etree_iterparse     | 63.5 ms                                                     | 60.0 ms: 1.06x faster                                                                  |
| fannkuch                | 258 ms                                                      | 245 ms: 1.05x faster                                                                   |
| regex_effbot            | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                                  |
| xml_etree_generate      | 54.5 ms                                                     | 52.4 ms: 1.04x faster                                                                  |
| unpickle_list           | 2.81 us                                                     | 2.71 us: 1.04x faster                                                                  |
| async_generators        | 224 ms                                                      | 217 ms: 1.03x faster                                                                   |
| sqlite_synth            | 1.84 us                                                     | 1.79 us: 1.03x faster                                                                  |
| nbody                   | 69.3 ms                                                     | 68.3 ms: 1.02x faster                                                                  |
| logging_format          | 6.66 us                                                     | 6.58 us: 1.01x faster                                                                  |
| telco                   | 3.78 ms                                                     | 3.82 ms: 1.01x slower                                                                  |
| unpack_sequence         | 37.8 ns                                                     | 38.4 ns: 1.01x slower                                                                  |
| pidigits                | 145 ms                                                      | 148 ms: 1.02x slower                                                                   |
| pathlib                 | 77.4 ms                                                     | 81.2 ms: 1.05x slower                                                                  |
| meteor_contest          | 72.5 ms                                                     | 76.2 ms: 1.05x slower                                                                  |
| gc_traversal            | 1.34 ms                                                     | 1.43 ms: 1.07x slower                                                                  |
| pickle_dict             | 16.9 us                                                     | 18.3 us: 1.08x slower                                                                  |
| pickle_list             | 2.59 us                                                     | 2.80 us: 1.08x slower                                                                  |
| bench_mp_pool           | 60.7 ms                                                     | 66.3 ms: 1.09x slower                                                                  |
| dask                    | 305 ms                                                      | 358 ms: 1.17x slower                                                                   |
| coverage                | 40.0 ms                                                     | 50.6 ms: 1.26x slower                                                                  |
| Geometric mean          | (ref)                                                       | 1.19x faster                                                                           |

Benchmark hidden because not significant (3): python_startup_no_site, logging_simple, pickle
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x
