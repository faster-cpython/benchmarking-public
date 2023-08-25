
# Results vs. 3.10.4

- fork: python
- ref: ef7c2bfcf1fd618438f9
- machine: windows-amd64
- commit hash: ef7c2bf
- commit date: 2023-02-05
- overall geometric mean: 1.21x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf1-amd64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 200 ms: 1.19x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.59 ms: 1.29x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.55 sec: 1.22x faster                                                      |
| html5lib       | 46.5 ms                                                     | 34.6 ms: 1.34x faster                                                       |
| tornado_http   | 109 ms                                                      | 92.2 ms: 1.18x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf1-amd64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 50.4 ms: 1.20x faster                                                       |
| nbody          | 69.3 ms                                                     | 61.4 ms: 1.13x faster                                                       |
| pidigits       | 145 ms                                                      | 152 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf1-amd64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 77.6 ms: 1.33x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.3 ms: 1.13x faster                                                       |
| regex_dna      | 132 ms                                                      | 119 ms: 1.11x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf1-amd64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.14 ms: 1.65x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 175 us: 1.47x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 122 us: 1.40x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 34.5 ms: 1.26x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 87.7 ms: 1.16x faster                                                       |
| json_loads           | 14.2 us                                                     | 12.9 us: 1.10x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 49.9 ms: 1.09x faster                                                       |
| unpickle             | 9.17 us                                                     | 9.39 us: 1.02x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.79 us: 1.08x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.7 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (3): unpickle_list, xml_etree_iterparse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf1-amd64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.8 ms: 1.07x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf1-amd64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.14 ms: 1.43x faster                                                       |
| django_template | 28.2 ms                                                     | 21.1 ms: 1.34x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 14.8 ms: 1.29x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 32.5 ms: 1.25x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf1-amd64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.02 ms: 2.06x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 57.2 ns: 1.69x faster                                                       |
| richards                | 41.2 ms                                                     | 24.5 ms: 1.68x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.14 ms: 1.65x faster                                                       |
| mypy2                   | 352 ms                                                      | 217 ms: 1.62x faster                                                        |
| scimark_sor             | 105 ms                                                      | 65.4 ms: 1.60x faster                                                       |
| go                      | 136 ms                                                      | 85.9 ms: 1.59x faster                                                       |
| raytrace                | 271 ms                                                      | 174 ms: 1.55x faster                                                        |
| pyflate                 | 387 ms                                                      | 259 ms: 1.49x faster                                                        |
| scimark_lu              | 85.4 ms                                                     | 57.5 ms: 1.48x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 481 ms: 1.48x faster                                                        |
| pickle_pure_python      | 257 us                                                      | 175 us: 1.47x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 38.4 ms: 1.45x faster                                                       |
| chaos                   | 58.9 ms                                                     | 40.9 ms: 1.44x faster                                                       |
| mako                    | 8.80 ms                                                     | 6.14 ms: 1.43x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 3.86 ms: 1.43x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 26.8 ns: 1.41x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 44.5 ms: 1.40x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 122 us: 1.40x faster                                                        |
| sqlglot_parse           | 1.22 ms                                                     | 891 us: 1.37x faster                                                        |
| async_tree_io           | 1.07 sec                                                    | 779 ms: 1.37x faster                                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 1.08 ms: 1.35x faster                                                       |
| async_tree_none         | 420 ms                                                      | 312 ms: 1.35x faster                                                        |
| thrift                  | 615 us                                                      | 457 us: 1.35x faster                                                        |
| html5lib                | 46.5 ms                                                     | 34.6 ms: 1.34x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 371 ms: 1.34x faster                                                        |
| django_template         | 28.2 ms                                                     | 21.1 ms: 1.34x faster                                                       |
| pycparser               | 868 ms                                                      | 648 ms: 1.34x faster                                                        |
| regex_compile           | 103 ms                                                      | 77.6 ms: 1.33x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 21.5 us: 1.33x faster                                                       |
| comprehensions          | 16.0 us                                                     | 12.3 us: 1.30x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 929 ms: 1.30x faster                                                        |
| chameleon               | 5.92 ms                                                     | 4.59 ms: 1.29x faster                                                       |
| async_generators        | 224 ms                                                      | 173 ms: 1.29x faster                                                        |
| genshi_text             | 19.0 ms                                                     | 14.8 ms: 1.29x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 60.8 ms: 1.28x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 462 ms: 1.28x faster                                                        |
| xml_etree_process       | 43.4 ms                                                     | 34.5 ms: 1.26x faster                                                       |
| genshi_xml              | 40.5 ms                                                     | 32.5 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 490 ms: 1.24x faster                                                        |
| docutils                | 1.89 sec                                                    | 1.55 sec: 1.22x faster                                                      |
| fannkuch                | 258 ms                                                      | 212 ms: 1.21x faster                                                        |
| sqlglot_optimize        | 39.0 ms                                                     | 32.5 ms: 1.20x faster                                                       |
| float                   | 60.2 ms                                                     | 50.4 ms: 1.20x faster                                                       |
| deepcopy                | 255 us                                                      | 214 us: 1.19x faster                                                        |
| nqueens                 | 67.0 ms                                                     | 56.3 ms: 1.19x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.24 ms: 1.19x faster                                                       |
| 2to3                    | 237 ms                                                      | 200 ms: 1.19x faster                                                        |
| tornado_http            | 109 ms                                                      | 92.2 ms: 1.18x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 12.5 ms: 1.18x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 40.6 ms: 1.17x faster                                                       |
| scimark_fft             | 193 ms                                                      | 166 ms: 1.16x faster                                                        |
| xml_etree_parse         | 102 ms                                                      | 87.7 ms: 1.16x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 175 ms: 1.15x faster                                                        |
| sympy_str               | 188 ms                                                      | 164 ms: 1.15x faster                                                        |
| sympy_expand            | 315 ms                                                      | 276 ms: 1.14x faster                                                        |
| deepcopy_reduce         | 2.16 us                                                     | 1.89 us: 1.14x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 836 us: 1.13x faster                                                        |
| mdp                     | 1.71 sec                                                    | 1.51 sec: 1.13x faster                                                      |
| regex_v8                | 15.0 ms                                                     | 13.3 ms: 1.13x faster                                                       |
| nbody                   | 69.3 ms                                                     | 61.4 ms: 1.13x faster                                                       |
| sympy_sum               | 104 ms                                                      | 92.8 ms: 1.12x faster                                                       |
| regex_dna               | 132 ms                                                      | 119 ms: 1.11x faster                                                        |
| json                    | 3.05 ms                                                     | 2.76 ms: 1.11x faster                                                       |
| json_loads              | 14.2 us                                                     | 12.9 us: 1.10x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 49.9 ms: 1.09x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 718 us: 1.09x faster                                                        |
| coroutines              | 15.9 ms                                                     | 14.7 ms: 1.09x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.8 ms: 1.07x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.78 us: 1.03x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 75.1 ms: 1.03x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 71.1 ms: 1.02x faster                                                       |
| logging_format          | 6.66 us                                                     | 6.58 us: 1.01x faster                                                       |
| telco                   | 3.78 ms                                                     | 3.77 ms: 1.00x faster                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| unpickle                | 9.17 us                                                     | 9.39 us: 1.02x slower                                                       |
| pidigits                | 145 ms                                                      | 152 ms: 1.05x slower                                                        |
| bench_mp_pool           | 60.7 ms                                                     | 63.9 ms: 1.05x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.45 ms: 1.08x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.79 us: 1.08x slower                                                       |
| generators              | 31.6 ms                                                     | 34.2 ms: 1.08x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 18.7 us: 1.10x slower                                                       |
| dask                    | 305 ms                                                      | 353 ms: 1.16x slower                                                        |
| coverage                | 40.0 ms                                                     | 53.9 ms: 1.35x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.21x faster                                                                |

Benchmark hidden because not significant (4): unpickle_list, xml_etree_iterparse, logging_simple, pickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x
