# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc2
- machine: darwin-arm64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.265x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 0.76x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 162 ms: 1.18x faster                                         |
| chameleon      | 6.26 ms                                                | 4.37 ms: 1.43x faster                                        |
| docutils       | 1.73 sec                                               | 1.47 sec: 1.18x faster                                       |
| html5lib       | 42.4 ms                                                | 31.9 ms: 1.33x faster                                        |
| Geometric mean | (ref)                                                  | 1.22x faster                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 214 ms: 1.82x faster                                         |
| async_tree_memoization  | 474 ms                                                 | 261 ms: 1.81x faster                                         |
| async_tree_io           | 980 ms                                                 | 559 ms: 1.75x faster                                         |
| async_tree_cpu_io_mixed | 649 ms                                                 | 473 ms: 1.37x faster                                         |
| Geometric mean          | (ref)                                                  | 1.68x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.6 ms: 1.54x faster                                        |
| float          | 69.0 ms                                                | 48.3 ms: 1.43x faster                                        |
| Geometric mean | (ref)                                                  | 1.30x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.8 ms: 1.39x faster                                        |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                         |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.01x slower                                        |
| regex_effbot   | 2.46 ms                                                | 2.61 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 182 us: 1.54x faster                                         |
| unpickle_pure_python | 194 us                                                 | 142 us: 1.37x faster                                         |
| json_dumps           | 8.11 ms                                                | 6.31 ms: 1.29x faster                                        |
| xml_etree_process    | 46.5 ms                                                | 37.6 ms: 1.24x faster                                        |
| tomli_loads          | 1.71 sec                                               | 1.46 sec: 1.17x faster                                       |
| xml_etree_generate   | 53.5 ms                                                | 53.1 ms: 1.01x faster                                        |
| xml_etree_iterparse  | 72.1 ms                                                | 73.0 ms: 1.01x slower                                        |
| json_loads           | 16.4 us                                                | 16.7 us: 1.02x slower                                        |
| unpickle             | 8.80 us                                                | 9.21 us: 1.05x slower                                        |
| unpickle_list        | 2.69 us                                                | 2.91 us: 1.08x slower                                        |
| pickle_dict          | 17.0 us                                                | 18.4 us: 1.09x slower                                        |
| pickle_list          | 2.74 us                                                | 3.01 us: 1.10x slower                                        |
| pickle               | 6.97 us                                                | 7.70 us: 1.10x slower                                        |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.2 ms: 1.58x slower                                        |
| python_startup_no_site | 7.91 ms                                                | 13.7 ms: 1.74x slower                                        |
| Geometric mean         | (ref)                                                  | 1.66x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.08 ms: 1.40x faster                                        |
| django_template | 26.4 ms                                                | 19.8 ms: 1.33x faster                                        |
| genshi_text     | 17.3 ms                                                | 14.1 ms: 1.23x faster                                        |
| genshi_xml      | 33.8 ms                                                | 30.2 ms: 1.12x faster                                        |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 89.7 us: 3.60x faster                                        |
| deltablue                | 4.91 ms                                                | 2.16 ms: 2.27x faster                                        |
| raytrace                 | 301 ms                                                 | 149 ms: 2.03x faster                                         |
| logging_silent           | 117 ns                                                 | 60.7 ns: 1.93x faster                                        |
| chaos                    | 65.8 ms                                                | 34.4 ms: 1.91x faster                                        |
| async_tree_none          | 388 ms                                                 | 214 ms: 1.82x faster                                         |
| async_tree_memoization   | 474 ms                                                 | 261 ms: 1.81x faster                                         |
| async_tree_io            | 980 ms                                                 | 559 ms: 1.75x faster                                         |
| sqlglot_parse            | 1.24 ms                                                | 739 us: 1.68x faster                                         |
| richards_super           | 57.8 ms                                                | 34.6 ms: 1.67x faster                                        |
| asyncio_tcp              | 659 ms                                                 | 408 ms: 1.62x faster                                         |
| sqlglot_transpile        | 1.44 ms                                                | 899 us: 1.60x faster                                         |
| comprehensions           | 16.9 us                                                | 10.6 us: 1.59x faster                                        |
| pylint                   | 277 ms                                                 | 179 ms: 1.55x faster                                         |
| richards                 | 48.7 ms                                                | 31.5 ms: 1.55x faster                                        |
| pickle_pure_python       | 281 us                                                 | 182 us: 1.54x faster                                         |
| nbody                    | 93.0 ms                                                | 60.6 ms: 1.54x faster                                        |
| scimark_monte_carlo      | 65.6 ms                                                | 42.8 ms: 1.53x faster                                        |
| scimark_lu               | 103 ms                                                 | 67.6 ms: 1.52x faster                                        |
| deepcopy_memo            | 34.7 us                                                | 23.0 us: 1.51x faster                                        |
| go                       | 151 ms                                                 | 101 ms: 1.50x faster                                         |
| hexiom                   | 6.19 ms                                                | 4.16 ms: 1.49x faster                                        |
| unpack_sequence          | 39.0 ns                                                | 26.7 ns: 1.46x faster                                        |
| crypto_pyaes             | 71.8 ms                                                | 49.9 ms: 1.44x faster                                        |
| chameleon                | 6.26 ms                                                | 4.37 ms: 1.43x faster                                        |
| float                    | 69.0 ms                                                | 48.3 ms: 1.43x faster                                        |
| logging_simple           | 4.45 us                                                | 3.12 us: 1.43x faster                                        |
| logging_format           | 4.83 us                                                | 3.39 us: 1.42x faster                                        |
| spectral_norm            | 94.8 ms                                                | 67.0 ms: 1.41x faster                                        |
| generators               | 32.3 ms                                                | 22.9 ms: 1.41x faster                                        |
| mako                     | 9.87 ms                                                | 7.08 ms: 1.40x faster                                        |
| regex_compile            | 95.3 ms                                                | 68.8 ms: 1.39x faster                                        |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 473 ms: 1.37x faster                                         |
| unpickle_pure_python     | 194 us                                                 | 142 us: 1.37x faster                                         |
| pprint_pformat           | 1.30 sec                                               | 953 ms: 1.37x faster                                         |
| pprint_safe_repr         | 641 ms                                                 | 468 ms: 1.37x faster                                         |
| pycparser                | 877 ms                                                 | 641 ms: 1.37x faster                                         |
| scimark_sor              | 128 ms                                                 | 95.5 ms: 1.34x faster                                        |
| django_template          | 26.4 ms                                                | 19.8 ms: 1.33x faster                                        |
| deepcopy                 | 272 us                                                 | 204 us: 1.33x faster                                         |
| html5lib                 | 42.4 ms                                                | 31.9 ms: 1.33x faster                                        |
| pyflate                  | 427 ms                                                 | 322 ms: 1.33x faster                                         |
| sympy_sum                | 92.2 ms                                                | 69.8 ms: 1.32x faster                                        |
| thrift                   | 572 us                                                 | 435 us: 1.31x faster                                         |
| coroutines               | 20.7 ms                                                | 16.0 ms: 1.30x faster                                        |
| dulwich_log              | 35.3 ms                                                | 27.3 ms: 1.29x faster                                        |
| json_dumps               | 8.11 ms                                                | 6.31 ms: 1.29x faster                                        |
| deepcopy_reduce          | 2.33 us                                                | 1.82 us: 1.28x faster                                        |
| mypy2                    | 607 ms                                                 | 479 ms: 1.27x faster                                         |
| sympy_integrate          | 13.1 ms                                                | 10.4 ms: 1.27x faster                                        |
| sympy_str                | 165 ms                                                 | 133 ms: 1.24x faster                                         |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                       |
| xml_etree_process        | 46.5 ms                                                | 37.6 ms: 1.24x faster                                        |
| genshi_text              | 17.3 ms                                                | 14.1 ms: 1.23x faster                                        |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                         |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.81 ms: 1.22x faster                                        |
| nqueens                  | 63.8 ms                                                | 52.9 ms: 1.20x faster                                        |
| 2to3                     | 192 ms                                                 | 162 ms: 1.18x faster                                         |
| docutils                 | 1.73 sec                                               | 1.47 sec: 1.18x faster                                       |
| sympy_expand             | 269 ms                                                 | 228 ms: 1.18x faster                                         |
| fannkuch                 | 303 ms                                                 | 257 ms: 1.18x faster                                         |
| sqlglot_optimize         | 36.8 ms                                                | 31.3 ms: 1.18x faster                                        |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                         |
| tomli_loads              | 1.71 sec                                               | 1.46 sec: 1.17x faster                                       |
| mdp                      | 1.63 sec                                               | 1.42 sec: 1.15x faster                                       |
| bench_thread_pool        | 527 us                                                 | 460 us: 1.15x faster                                         |
| gunicorn                 | 1.30 ms                                                | 1.14 ms: 1.14x faster                                        |
| sqlglot_normalize        | 190 ms                                                 | 168 ms: 1.13x faster                                         |
| genshi_xml               | 33.8 ms                                                | 30.2 ms: 1.12x faster                                        |
| meteor_contest           | 77.7 ms                                                | 71.6 ms: 1.09x faster                                        |
| dask                     | 253 ms                                                 | 234 ms: 1.08x faster                                         |
| json                     | 3.08 ms                                                | 2.95 ms: 1.04x faster                                        |
| xml_etree_generate       | 53.5 ms                                                | 53.1 ms: 1.01x faster                                        |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                         |
| xml_etree_iterparse      | 72.1 ms                                                | 73.0 ms: 1.01x slower                                        |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.01x slower                                        |
| json_loads               | 16.4 us                                                | 16.7 us: 1.02x slower                                        |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                        |
| create_gc_cycles         | 860 us                                                 | 898 us: 1.04x slower                                         |
| unpickle                 | 8.80 us                                                | 9.21 us: 1.05x slower                                        |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.06x slower                                        |
| regex_effbot             | 2.46 ms                                                | 2.61 ms: 1.06x slower                                        |
| coverage                 | 41.5 ms                                                | 44.7 ms: 1.08x slower                                        |
| unpickle_list            | 2.69 us                                                | 2.91 us: 1.08x slower                                        |
| pickle_dict              | 17.0 us                                                | 18.4 us: 1.09x slower                                        |
| pickle_list              | 2.74 us                                                | 3.01 us: 1.10x slower                                        |
| pickle                   | 6.97 us                                                | 7.70 us: 1.10x slower                                        |
| async_generators         | 231 ms                                                 | 285 ms: 1.23x slower                                         |
| bench_mp_pool            | 37.4 ms                                                | 49.0 ms: 1.31x slower                                        |
| telco                    | 3.49 ms                                                | 4.69 ms: 1.34x slower                                        |
| flaskblogging            | 2.65 ms                                                | 3.96 ms: 1.50x slower                                        |
| python_startup           | 10.9 ms                                                | 17.2 ms: 1.58x slower                                        |
| python_startup_no_site   | 7.91 ms                                                | 13.7 ms: 1.74x slower                                        |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                 |

Benchmark hidden because not significant (5): aiohttp, tornado_http, xml_etree_parse, pidigits, pathlib
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.265x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 0.76x