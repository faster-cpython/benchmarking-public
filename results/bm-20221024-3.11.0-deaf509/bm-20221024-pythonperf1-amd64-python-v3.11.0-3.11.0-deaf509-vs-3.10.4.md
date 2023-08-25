
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0
- machine: windows-amd64
- commit hash: deaf509
- commit date: 2022-10-24
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 209 ms: 1.13x faster                                        |
| chameleon      | 5.92 ms                                                     | 5.11 ms: 1.16x faster                                       |
| docutils       | 1.89 sec                                                    | 1.60 sec: 1.18x faster                                      |
| html5lib       | 46.5 ms                                                     | 37.5 ms: 1.24x faster                                       |
| tornado_http   | 109 ms                                                      | 91.8 ms: 1.19x faster                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 54.6 ms: 1.10x faster                                       |
| nbody          | 69.3 ms                                                     | 70.0 ms: 1.01x slower                                       |
| pidigits       | 145 ms                                                      | 148 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_dna      | 132 ms                                                      | 115 ms: 1.14x faster                                        |
| regex_compile  | 103 ms                                                      | 90.6 ms: 1.14x faster                                       |
| regex_effbot   | 1.66 ms                                                     | 1.50 ms: 1.11x faster                                       |
| regex_v8       | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_pure_python   | 257 us                                                      | 200 us: 1.28x faster                                        |
| xml_etree_process    | 43.4 ms                                                     | 37.1 ms: 1.17x faster                                       |
| tomli_loads          | 1.62 sec                                                    | 1.41 sec: 1.15x faster                                      |
| unpickle             | 9.17 us                                                     | 8.09 us: 1.13x faster                                       |
| unpickle_pure_python | 171 us                                                      | 152 us: 1.13x faster                                        |
| json_dumps           | 8.50 ms                                                     | 7.56 ms: 1.12x faster                                       |
| unpickle_list        | 2.81 us                                                     | 2.55 us: 1.10x faster                                       |
| json_loads           | 14.2 us                                                     | 12.9 us: 1.10x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 95.9 ms: 1.06x faster                                       |
| xml_etree_generate   | 54.5 ms                                                     | 52.2 ms: 1.04x faster                                       |
| pickle               | 6.80 us                                                     | 6.61 us: 1.03x faster                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 62.6 ms: 1.01x faster                                       |
| pickle_list          | 2.59 us                                                     | 2.68 us: 1.04x slower                                       |
| pickle_dict          | 16.9 us                                                     | 18.5 us: 1.09x slower                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.7 ms: 1.07x faster                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.9 ms: 1.02x slower                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 7.26 ms: 1.21x faster                                       |
| django_template | 28.2 ms                                                     | 24.1 ms: 1.17x faster                                       |
| genshi_text     | 19.0 ms                                                     | 17.0 ms: 1.12x faster                                       |
| genshi_xml      | 40.5 ms                                                     | 37.3 ms: 1.09x faster                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| deltablue                | 4.17 ms                                                     | 2.61 ms: 1.60x faster                                       |
| mypy2                    | 352 ms                                                      | 229 ms: 1.54x faster                                        |
| go                       | 136 ms                                                      | 97.3 ms: 1.40x faster                                       |
| scimark_sor              | 105 ms                                                      | 75.6 ms: 1.39x faster                                       |
| logging_silent           | 96.4 ns                                                     | 69.8 ns: 1.38x faster                                       |
| richards_super           | 51.7 ms                                                     | 37.5 ms: 1.38x faster                                       |
| async_tree_io            | 1.07 sec                                                    | 779 ms: 1.37x faster                                        |
| richards                 | 41.2 ms                                                     | 30.6 ms: 1.35x faster                                       |
| scimark_lu               | 85.4 ms                                                     | 63.5 ms: 1.34x faster                                       |
| async_tree_memoization   | 497 ms                                                      | 371 ms: 1.34x faster                                        |
| async_tree_none          | 420 ms                                                      | 320 ms: 1.31x faster                                        |
| crypto_pyaes             | 62.3 ms                                                     | 47.6 ms: 1.31x faster                                       |
| raytrace                 | 271 ms                                                      | 211 ms: 1.29x faster                                        |
| pickle_pure_python       | 257 us                                                      | 200 us: 1.28x faster                                        |
| sqlglot_parse            | 1.22 ms                                                     | 952 us: 1.28x faster                                        |
| pyflate                  | 387 ms                                                      | 304 ms: 1.27x faster                                        |
| async_generators         | 224 ms                                                      | 178 ms: 1.26x faster                                        |
| sqlglot_transpile        | 1.46 ms                                                     | 1.16 ms: 1.26x faster                                       |
| pycparser                | 868 ms                                                      | 691 ms: 1.26x faster                                        |
| thrift                   | 615 us                                                      | 491 us: 1.25x faster                                        |
| scimark_monte_carlo      | 55.9 ms                                                     | 44.6 ms: 1.25x faster                                       |
| chaos                    | 58.9 ms                                                     | 47.1 ms: 1.25x faster                                       |
| html5lib                 | 46.5 ms                                                     | 37.5 ms: 1.24x faster                                       |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 501 ms: 1.22x faster                                        |
| hexiom                   | 5.52 ms                                                     | 4.55 ms: 1.21x faster                                       |
| mako                     | 8.80 ms                                                     | 7.26 ms: 1.21x faster                                       |
| tornado_http             | 109 ms                                                      | 91.8 ms: 1.19x faster                                       |
| docutils                 | 1.89 sec                                                    | 1.60 sec: 1.18x faster                                      |
| xml_etree_process        | 43.4 ms                                                     | 37.1 ms: 1.17x faster                                       |
| django_template          | 28.2 ms                                                     | 24.1 ms: 1.17x faster                                       |
| sqlalchemy_declarative   | 95.4 ms                                                     | 81.5 ms: 1.17x faster                                       |
| pprint_pformat           | 1.21 sec                                                    | 1.04 sec: 1.16x faster                                      |
| chameleon                | 5.92 ms                                                     | 5.11 ms: 1.16x faster                                       |
| dask                     | 305 ms                                                      | 264 ms: 1.15x faster                                        |
| pprint_safe_repr         | 589 ms                                                      | 512 ms: 1.15x faster                                        |
| spectral_norm            | 78.0 ms                                                     | 67.9 ms: 1.15x faster                                       |
| tomli_loads              | 1.62 sec                                                    | 1.41 sec: 1.15x faster                                      |
| regex_dna                | 132 ms                                                      | 115 ms: 1.14x faster                                        |
| regex_compile            | 103 ms                                                      | 90.6 ms: 1.14x faster                                       |
| unpickle                 | 9.17 us                                                     | 8.09 us: 1.13x faster                                       |
| 2to3                     | 237 ms                                                      | 209 ms: 1.13x faster                                        |
| deepcopy_memo            | 28.5 us                                                     | 25.2 us: 1.13x faster                                       |
| create_gc_cycles         | 782 us                                                      | 693 us: 1.13x faster                                        |
| unpickle_pure_python     | 171 us                                                      | 152 us: 1.13x faster                                        |
| json_dumps               | 8.50 ms                                                     | 7.56 ms: 1.12x faster                                       |
| genshi_text              | 19.0 ms                                                     | 17.0 ms: 1.12x faster                                       |
| aiohttp                  | 1.01 ms                                                     | 899 us: 1.12x faster                                        |
| sqlglot_optimize         | 39.0 ms                                                     | 34.9 ms: 1.12x faster                                       |
| regex_effbot             | 1.66 ms                                                     | 1.50 ms: 1.11x faster                                       |
| bench_thread_pool        | 946 us                                                      | 852 us: 1.11x faster                                        |
| unpickle_list            | 2.81 us                                                     | 2.55 us: 1.10x faster                                       |
| float                    | 60.2 ms                                                     | 54.6 ms: 1.10x faster                                       |
| json_loads               | 14.2 us                                                     | 12.9 us: 1.10x faster                                       |
| sqlite_synth             | 1.84 us                                                     | 1.68 us: 1.09x faster                                       |
| coroutines               | 15.9 ms                                                     | 14.6 ms: 1.09x faster                                       |
| genshi_xml               | 40.5 ms                                                     | 37.3 ms: 1.09x faster                                       |
| regex_v8                 | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                       |
| pathlib                  | 77.4 ms                                                     | 71.4 ms: 1.08x faster                                       |
| scimark_fft              | 193 ms                                                      | 178 ms: 1.08x faster                                        |
| sqlalchemy_imperative    | 11.0 ms                                                     | 10.2 ms: 1.08x faster                                       |
| sympy_integrate          | 14.8 ms                                                     | 13.8 ms: 1.07x faster                                       |
| dulwich_log              | 47.6 ms                                                     | 44.5 ms: 1.07x faster                                       |
| python_startup           | 20.0 ms                                                     | 18.7 ms: 1.07x faster                                       |
| sympy_expand             | 315 ms                                                      | 295 ms: 1.07x faster                                        |
| pylint                   | 347 ms                                                      | 326 ms: 1.06x faster                                        |
| sqlglot_normalize        | 202 ms                                                      | 190 ms: 1.06x faster                                        |
| xml_etree_parse          | 102 ms                                                      | 95.9 ms: 1.06x faster                                       |
| xml_etree_generate       | 54.5 ms                                                     | 52.2 ms: 1.04x faster                                       |
| sympy_sum                | 104 ms                                                      | 99.9 ms: 1.04x faster                                       |
| deepcopy_reduce          | 2.16 us                                                     | 2.07 us: 1.04x faster                                       |
| deepcopy                 | 255 us                                                      | 246 us: 1.04x faster                                        |
| sympy_str                | 188 ms                                                      | 182 ms: 1.03x faster                                        |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.57 ms: 1.03x faster                                       |
| nqueens                  | 67.0 ms                                                     | 64.9 ms: 1.03x faster                                       |
| pickle                   | 6.80 us                                                     | 6.61 us: 1.03x faster                                       |
| mdp                      | 1.71 sec                                                    | 1.67 sec: 1.03x faster                                      |
| fannkuch                 | 258 ms                                                      | 252 ms: 1.02x faster                                        |
| xml_etree_iterparse      | 63.5 ms                                                     | 62.6 ms: 1.01x faster                                       |
| typing_runtime_protocols | 325 us                                                      | 322 us: 1.01x faster                                        |
| nbody                    | 69.3 ms                                                     | 70.0 ms: 1.01x slower                                       |
| pidigits                 | 145 ms                                                      | 148 ms: 1.02x slower                                        |
| python_startup_no_site   | 15.5 ms                                                     | 15.9 ms: 1.02x slower                                       |
| bench_mp_pool            | 60.7 ms                                                     | 62.5 ms: 1.03x slower                                       |
| meteor_contest           | 72.5 ms                                                     | 74.7 ms: 1.03x slower                                       |
| telco                    | 3.78 ms                                                     | 3.90 ms: 1.03x slower                                       |
| pickle_list              | 2.59 us                                                     | 2.68 us: 1.04x slower                                       |
| logging_format           | 6.66 us                                                     | 7.01 us: 1.05x slower                                       |
| logging_simple           | 6.20 us                                                     | 6.61 us: 1.07x slower                                       |
| json                     | 3.05 ms                                                     | 3.25 ms: 1.07x slower                                       |
| generators               | 31.6 ms                                                     | 33.8 ms: 1.07x slower                                       |
| gc_traversal             | 1.34 ms                                                     | 1.46 ms: 1.08x slower                                       |
| pickle_dict              | 16.9 us                                                     | 18.5 us: 1.09x slower                                       |
| unpack_sequence          | 37.8 ns                                                     | 46.1 ns: 1.22x slower                                       |
| coverage                 | 40.0 ms                                                     | 55.9 ms: 1.40x slower                                       |
| Geometric mean           | (ref)                                                       | 1.12x faster                                                |

Benchmark hidden because not significant (4): asyncio_tcp, comprehensions, flaskblogging, asyncio_tcp_ssl


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x
