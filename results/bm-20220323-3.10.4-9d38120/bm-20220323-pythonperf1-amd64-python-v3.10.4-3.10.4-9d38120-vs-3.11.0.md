
# Results vs. 3.11.0

- fork: python
- ref: v3.10.4
- machine: windows-amd64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.12x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 237 ms: 1.13x slower                                        |
| chameleon      | 5.11 ms                                                     | 5.92 ms: 1.16x slower                                       |
| docutils       | 1.60 sec                                                    | 1.89 sec: 1.18x slower                                      |
| html5lib       | 37.5 ms                                                     | 46.5 ms: 1.24x slower                                       |
| tornado_http   | 91.8 ms                                                     | 109 ms: 1.19x slower                                        |
| Geometric mean | (ref)                                                       | 1.18x slower                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 145 ms: 1.02x faster                                        |
| nbody          | 70.0 ms                                                     | 69.3 ms: 1.01x faster                                       |
| float          | 54.6 ms                                                     | 60.2 ms: 1.10x slower                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 15.0 ms: 1.09x slower                                       |
| regex_effbot   | 1.50 ms                                                     | 1.66 ms: 1.11x slower                                       |
| regex_compile  | 90.6 ms                                                     | 103 ms: 1.14x slower                                        |
| regex_dna      | 115 ms                                                      | 132 ms: 1.14x slower                                        |
| Geometric mean | (ref)                                                       | 1.12x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_dict          | 18.5 us                                                     | 16.9 us: 1.09x faster                                       |
| pickle_list          | 2.68 us                                                     | 2.59 us: 1.04x faster                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.5 ms: 1.01x slower                                       |
| pickle               | 6.61 us                                                     | 6.80 us: 1.03x slower                                       |
| xml_etree_generate   | 52.2 ms                                                     | 54.5 ms: 1.04x slower                                       |
| xml_etree_parse      | 95.9 ms                                                     | 102 ms: 1.06x slower                                        |
| json_loads           | 12.9 us                                                     | 14.2 us: 1.10x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.81 us: 1.10x slower                                       |
| json_dumps           | 7.56 ms                                                     | 8.50 ms: 1.12x slower                                       |
| unpickle_pure_python | 152 us                                                      | 171 us: 1.13x slower                                        |
| unpickle             | 8.09 us                                                     | 9.17 us: 1.13x slower                                       |
| tomli_loads          | 1.41 sec                                                    | 1.62 sec: 1.15x slower                                      |
| xml_etree_process    | 37.1 ms                                                     | 43.4 ms: 1.17x slower                                       |
| pickle_pure_python   | 200 us                                                      | 257 us: 1.28x slower                                        |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.5 ms: 1.02x faster                                       |
| python_startup         | 18.7 ms                                                     | 20.0 ms: 1.07x slower                                       |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_xml      | 37.3 ms                                                     | 40.5 ms: 1.09x slower                                       |
| genshi_text     | 17.0 ms                                                     | 19.0 ms: 1.12x slower                                       |
| django_template | 24.1 ms                                                     | 28.2 ms: 1.17x slower                                       |
| mako            | 7.26 ms                                                     | 8.80 ms: 1.21x slower                                       |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| coverage                 | 55.9 ms                                                     | 40.0 ms: 1.40x faster                                       |
| unpack_sequence          | 46.1 ns                                                     | 37.8 ns: 1.22x faster                                       |
| pickle_dict              | 18.5 us                                                     | 16.9 us: 1.09x faster                                       |
| gc_traversal             | 1.46 ms                                                     | 1.34 ms: 1.08x faster                                       |
| generators               | 33.8 ms                                                     | 31.6 ms: 1.07x faster                                       |
| json                     | 3.25 ms                                                     | 3.05 ms: 1.07x faster                                       |
| logging_simple           | 6.61 us                                                     | 6.20 us: 1.07x faster                                       |
| logging_format           | 7.01 us                                                     | 6.66 us: 1.05x faster                                       |
| pickle_list              | 2.68 us                                                     | 2.59 us: 1.04x faster                                       |
| telco                    | 3.90 ms                                                     | 3.78 ms: 1.03x faster                                       |
| meteor_contest           | 74.7 ms                                                     | 72.5 ms: 1.03x faster                                       |
| bench_mp_pool            | 62.5 ms                                                     | 60.7 ms: 1.03x faster                                       |
| python_startup_no_site   | 15.9 ms                                                     | 15.5 ms: 1.02x faster                                       |
| pidigits                 | 148 ms                                                      | 145 ms: 1.02x faster                                        |
| nbody                    | 70.0 ms                                                     | 69.3 ms: 1.01x faster                                       |
| typing_runtime_protocols | 322 us                                                      | 325 us: 1.01x slower                                        |
| xml_etree_iterparse      | 62.6 ms                                                     | 63.5 ms: 1.01x slower                                       |
| fannkuch                 | 252 ms                                                      | 258 ms: 1.02x slower                                        |
| mdp                      | 1.67 sec                                                    | 1.71 sec: 1.03x slower                                      |
| pickle                   | 6.61 us                                                     | 6.80 us: 1.03x slower                                       |
| nqueens                  | 64.9 ms                                                     | 67.0 ms: 1.03x slower                                       |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.66 ms: 1.03x slower                                       |
| sympy_str                | 182 ms                                                      | 188 ms: 1.03x slower                                        |
| deepcopy                 | 246 us                                                      | 255 us: 1.04x slower                                        |
| deepcopy_reduce          | 2.07 us                                                     | 2.16 us: 1.04x slower                                       |
| sympy_sum                | 99.9 ms                                                     | 104 ms: 1.04x slower                                        |
| xml_etree_generate       | 52.2 ms                                                     | 54.5 ms: 1.04x slower                                       |
| xml_etree_parse          | 95.9 ms                                                     | 102 ms: 1.06x slower                                        |
| sqlglot_normalize        | 190 ms                                                      | 202 ms: 1.06x slower                                        |
| pylint                   | 326 ms                                                      | 347 ms: 1.06x slower                                        |
| sympy_expand             | 295 ms                                                      | 315 ms: 1.07x slower                                        |
| python_startup           | 18.7 ms                                                     | 20.0 ms: 1.07x slower                                       |
| dulwich_log              | 44.5 ms                                                     | 47.6 ms: 1.07x slower                                       |
| sympy_integrate          | 13.8 ms                                                     | 14.8 ms: 1.07x slower                                       |
| sqlalchemy_imperative    | 10.2 ms                                                     | 11.0 ms: 1.08x slower                                       |
| scimark_fft              | 178 ms                                                      | 193 ms: 1.08x slower                                        |
| pathlib                  | 71.4 ms                                                     | 77.4 ms: 1.08x slower                                       |
| regex_v8                 | 13.8 ms                                                     | 15.0 ms: 1.09x slower                                       |
| genshi_xml               | 37.3 ms                                                     | 40.5 ms: 1.09x slower                                       |
| coroutines               | 14.6 ms                                                     | 15.9 ms: 1.09x slower                                       |
| sqlite_synth             | 1.68 us                                                     | 1.84 us: 1.09x slower                                       |
| json_loads               | 12.9 us                                                     | 14.2 us: 1.10x slower                                       |
| float                    | 54.6 ms                                                     | 60.2 ms: 1.10x slower                                       |
| unpickle_list            | 2.55 us                                                     | 2.81 us: 1.10x slower                                       |
| bench_thread_pool        | 852 us                                                      | 946 us: 1.11x slower                                        |
| regex_effbot             | 1.50 ms                                                     | 1.66 ms: 1.11x slower                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 39.0 ms: 1.12x slower                                       |
| aiohttp                  | 899 us                                                      | 1.01 ms: 1.12x slower                                       |
| genshi_text              | 17.0 ms                                                     | 19.0 ms: 1.12x slower                                       |
| json_dumps               | 7.56 ms                                                     | 8.50 ms: 1.12x slower                                       |
| unpickle_pure_python     | 152 us                                                      | 171 us: 1.13x slower                                        |
| create_gc_cycles         | 693 us                                                      | 782 us: 1.13x slower                                        |
| deepcopy_memo            | 25.2 us                                                     | 28.5 us: 1.13x slower                                       |
| 2to3                     | 209 ms                                                      | 237 ms: 1.13x slower                                        |
| unpickle                 | 8.09 us                                                     | 9.17 us: 1.13x slower                                       |
| regex_compile            | 90.6 ms                                                     | 103 ms: 1.14x slower                                        |
| regex_dna                | 115 ms                                                      | 132 ms: 1.14x slower                                        |
| tomli_loads              | 1.41 sec                                                    | 1.62 sec: 1.15x slower                                      |
| spectral_norm            | 67.9 ms                                                     | 78.0 ms: 1.15x slower                                       |
| pprint_safe_repr         | 512 ms                                                      | 589 ms: 1.15x slower                                        |
| dask                     | 264 ms                                                      | 305 ms: 1.15x slower                                        |
| chameleon                | 5.11 ms                                                     | 5.92 ms: 1.16x slower                                       |
| pprint_pformat           | 1.04 sec                                                    | 1.21 sec: 1.16x slower                                      |
| sqlalchemy_declarative   | 81.5 ms                                                     | 95.4 ms: 1.17x slower                                       |
| django_template          | 24.1 ms                                                     | 28.2 ms: 1.17x slower                                       |
| xml_etree_process        | 37.1 ms                                                     | 43.4 ms: 1.17x slower                                       |
| docutils                 | 1.60 sec                                                    | 1.89 sec: 1.18x slower                                      |
| tornado_http             | 91.8 ms                                                     | 109 ms: 1.19x slower                                        |
| mako                     | 7.26 ms                                                     | 8.80 ms: 1.21x slower                                       |
| hexiom                   | 4.55 ms                                                     | 5.52 ms: 1.21x slower                                       |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 609 ms: 1.22x slower                                        |
| html5lib                 | 37.5 ms                                                     | 46.5 ms: 1.24x slower                                       |
| chaos                    | 47.1 ms                                                     | 58.9 ms: 1.25x slower                                       |
| scimark_monte_carlo      | 44.6 ms                                                     | 55.9 ms: 1.25x slower                                       |
| thrift                   | 491 us                                                      | 615 us: 1.25x slower                                        |
| pycparser                | 691 ms                                                      | 868 ms: 1.26x slower                                        |
| sqlglot_transpile        | 1.16 ms                                                     | 1.46 ms: 1.26x slower                                       |
| async_generators         | 178 ms                                                      | 224 ms: 1.26x slower                                        |
| pyflate                  | 304 ms                                                      | 387 ms: 1.27x slower                                        |
| sqlglot_parse            | 952 us                                                      | 1.22 ms: 1.28x slower                                       |
| pickle_pure_python       | 200 us                                                      | 257 us: 1.28x slower                                        |
| raytrace                 | 211 ms                                                      | 271 ms: 1.29x slower                                        |
| crypto_pyaes             | 47.6 ms                                                     | 62.3 ms: 1.31x slower                                       |
| async_tree_none          | 320 ms                                                      | 420 ms: 1.31x slower                                        |
| async_tree_memoization   | 371 ms                                                      | 497 ms: 1.34x slower                                        |
| scimark_lu               | 63.5 ms                                                     | 85.4 ms: 1.34x slower                                       |
| richards                 | 30.6 ms                                                     | 41.2 ms: 1.35x slower                                       |
| async_tree_io            | 779 ms                                                      | 1.07 sec: 1.37x slower                                      |
| richards_super           | 37.5 ms                                                     | 51.7 ms: 1.38x slower                                       |
| logging_silent           | 69.8 ns                                                     | 96.4 ns: 1.38x slower                                       |
| scimark_sor              | 75.6 ms                                                     | 105 ms: 1.39x slower                                        |
| go                       | 97.3 ms                                                     | 136 ms: 1.40x slower                                        |
| mypy2                    | 229 ms                                                      | 352 ms: 1.54x slower                                        |
| deltablue                | 2.61 ms                                                     | 4.17 ms: 1.60x slower                                       |
| Geometric mean           | (ref)                                                       | 1.12x slower                                                |

Benchmark hidden because not significant (4): asyncio_tcp_ssl, flaskblogging, comprehensions, asyncio_tcp
