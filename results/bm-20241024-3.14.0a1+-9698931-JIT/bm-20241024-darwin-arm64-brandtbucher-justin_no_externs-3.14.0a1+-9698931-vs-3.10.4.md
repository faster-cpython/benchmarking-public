# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: darwin-arm64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.201x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.42x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 1.73 sec                                               | 1.58 sec: 1.10x faster                                                    |
| html5lib       | 42.4 ms                                                | 33.0 ms: 1.28x faster                                                     |
| tornado_http   | 86.7 ms                                                | 74.9 ms: 1.16x faster                                                     |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 200 ms: 1.94x faster                                                      |
| async_tree_memoization  | 474 ms                                                 | 246 ms: 1.92x faster                                                      |
| async_tree_io           | 980 ms                                                 | 586 ms: 1.67x faster                                                      |
| async_tree_cpu_io_mixed | 649 ms                                                 | 457 ms: 1.42x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 66.1 ms: 1.41x faster                                                     |
| float          | 69.0 ms                                                | 49.8 ms: 1.39x faster                                                     |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.25x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 142 ms: 1.23x faster                                                      |
| regex_compile  | 95.3 ms                                                | 79.4 ms: 1.20x faster                                                     |
| regex_v8       | 17.1 ms                                                | 16.7 ms: 1.03x faster                                                     |
| regex_effbot   | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 181 us: 1.55x faster                                                      |
| unpickle_pure_python | 194 us                                                 | 137 us: 1.42x faster                                                      |
| xml_etree_process    | 46.5 ms                                                | 35.7 ms: 1.30x faster                                                     |
| tomli_loads          | 1.71 sec                                               | 1.33 sec: 1.28x faster                                                    |
| json_dumps           | 8.11 ms                                                | 7.23 ms: 1.12x faster                                                     |
| xml_etree_generate   | 53.5 ms                                                | 51.2 ms: 1.04x faster                                                     |
| json_loads           | 16.4 us                                                | 16.6 us: 1.01x slower                                                     |
| xml_etree_iterparse  | 72.1 ms                                                | 73.9 ms: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 18.0 ms: 1.65x slower                                                     |
| python_startup_no_site | 7.91 ms                                                | 14.0 ms: 1.77x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.71x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.03 ms: 1.40x faster                                                     |
| django_template | 26.4 ms                                                | 25.0 ms: 1.06x faster                                                     |
| genshi_text     | 17.3 ms                                                | 16.8 ms: 1.03x faster                                                     |
| genshi_xml      | 33.8 ms                                                | 45.7 ms: 1.35x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 99.5 us: 3.25x faster                                                     |
| deltablue                | 4.91 ms                                                | 2.51 ms: 1.96x faster                                                     |
| async_tree_none          | 388 ms                                                 | 200 ms: 1.94x faster                                                      |
| async_tree_memoization   | 474 ms                                                 | 246 ms: 1.92x faster                                                      |
| deepcopy_memo            | 34.7 us                                                | 18.1 us: 1.92x faster                                                     |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                      |
| raytrace                 | 301 ms                                                 | 178 ms: 1.69x faster                                                      |
| async_tree_io            | 980 ms                                                 | 586 ms: 1.67x faster                                                      |
| deepcopy                 | 272 us                                                 | 163 us: 1.67x faster                                                      |
| logging_silent           | 117 ns                                                 | 74.8 ns: 1.57x faster                                                     |
| scimark_lu               | 103 ms                                                 | 66.1 ms: 1.56x faster                                                     |
| pickle_pure_python       | 281 us                                                 | 181 us: 1.55x faster                                                      |
| deepcopy_reduce          | 2.33 us                                                | 1.54 us: 1.52x faster                                                     |
| chaos                    | 65.8 ms                                                | 43.7 ms: 1.51x faster                                                     |
| richards_super           | 57.8 ms                                                | 40.1 ms: 1.44x faster                                                     |
| unpickle_pure_python     | 194 us                                                 | 137 us: 1.42x faster                                                      |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 457 ms: 1.42x faster                                                      |
| go                       | 151 ms                                                 | 106 ms: 1.42x faster                                                      |
| nbody                    | 93.0 ms                                                | 66.1 ms: 1.41x faster                                                     |
| mako                     | 9.87 ms                                                | 7.03 ms: 1.40x faster                                                     |
| scimark_sor              | 128 ms                                                 | 91.6 ms: 1.40x faster                                                     |
| logging_simple           | 4.45 us                                                | 3.18 us: 1.40x faster                                                     |
| logging_format           | 4.83 us                                                | 3.48 us: 1.39x faster                                                     |
| float                    | 69.0 ms                                                | 49.8 ms: 1.39x faster                                                     |
| scimark_monte_carlo      | 65.6 ms                                                | 47.9 ms: 1.37x faster                                                     |
| sqlglot_parse            | 1.24 ms                                                | 916 us: 1.36x faster                                                      |
| thrift                   | 572 us                                                 | 422 us: 1.36x faster                                                      |
| richards                 | 48.7 ms                                                | 36.0 ms: 1.35x faster                                                     |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.73 ms: 1.32x faster                                                     |
| xml_etree_process        | 46.5 ms                                                | 35.7 ms: 1.30x faster                                                     |
| crypto_pyaes             | 71.8 ms                                                | 55.6 ms: 1.29x faster                                                     |
| spectral_norm            | 94.8 ms                                                | 73.6 ms: 1.29x faster                                                     |
| sqlglot_transpile        | 1.44 ms                                                | 1.12 ms: 1.28x faster                                                     |
| tomli_loads              | 1.71 sec                                               | 1.33 sec: 1.28x faster                                                    |
| html5lib                 | 42.4 ms                                                | 33.0 ms: 1.28x faster                                                     |
| pylint                   | 277 ms                                                 | 217 ms: 1.27x faster                                                      |
| coroutines               | 20.7 ms                                                | 16.3 ms: 1.27x faster                                                     |
| pycparser                | 877 ms                                                 | 705 ms: 1.24x faster                                                      |
| pyflate                  | 427 ms                                                 | 343 ms: 1.24x faster                                                      |
| generators               | 32.3 ms                                                | 26.0 ms: 1.24x faster                                                     |
| regex_dna                | 174 ms                                                 | 142 ms: 1.23x faster                                                      |
| pprint_safe_repr         | 641 ms                                                 | 533 ms: 1.20x faster                                                      |
| regex_compile            | 95.3 ms                                                | 79.4 ms: 1.20x faster                                                     |
| dulwich_log              | 35.3 ms                                                | 29.8 ms: 1.18x faster                                                     |
| comprehensions           | 16.9 us                                                | 14.3 us: 1.18x faster                                                     |
| sqlalchemy_declarative   | 73.3 ms                                                | 62.4 ms: 1.17x faster                                                     |
| tornado_http             | 86.7 ms                                                | 74.9 ms: 1.16x faster                                                     |
| pprint_pformat           | 1.30 sec                                               | 1.13 sec: 1.15x faster                                                    |
| hexiom                   | 6.19 ms                                                | 5.52 ms: 1.12x faster                                                     |
| json_dumps               | 8.11 ms                                                | 7.23 ms: 1.12x faster                                                     |
| sympy_sum                | 92.2 ms                                                | 82.6 ms: 1.12x faster                                                     |
| scimark_fft              | 224 ms                                                 | 203 ms: 1.11x faster                                                      |
| fannkuch                 | 303 ms                                                 | 275 ms: 1.10x faster                                                      |
| docutils                 | 1.73 sec                                               | 1.58 sec: 1.10x faster                                                    |
| bench_thread_pool        | 527 us                                                 | 481 us: 1.10x faster                                                      |
| pathlib                  | 24.5 ms                                                | 22.4 ms: 1.09x faster                                                     |
| json                     | 3.08 ms                                                | 2.87 ms: 1.08x faster                                                     |
| django_template          | 26.4 ms                                                | 25.0 ms: 1.06x faster                                                     |
| sympy_expand             | 269 ms                                                 | 256 ms: 1.05x faster                                                      |
| sympy_str                | 165 ms                                                 | 158 ms: 1.05x faster                                                      |
| mdp                      | 1.63 sec                                               | 1.55 sec: 1.05x faster                                                    |
| xml_etree_generate       | 53.5 ms                                                | 51.2 ms: 1.04x faster                                                     |
| nqueens                  | 63.8 ms                                                | 61.6 ms: 1.03x faster                                                     |
| genshi_text              | 17.3 ms                                                | 16.8 ms: 1.03x faster                                                     |
| regex_v8                 | 17.1 ms                                                | 16.7 ms: 1.03x faster                                                     |
| meteor_contest           | 77.7 ms                                                | 76.8 ms: 1.01x faster                                                     |
| regex_effbot             | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                     |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                      |
| sympy_integrate          | 13.1 ms                                                | 13.2 ms: 1.01x slower                                                     |
| json_loads               | 16.4 us                                                | 16.6 us: 1.01x slower                                                     |
| sqlglot_normalize        | 190 ms                                                 | 195 ms: 1.02x slower                                                      |
| xml_etree_iterparse      | 72.1 ms                                                | 73.9 ms: 1.02x slower                                                     |
| coverage                 | 41.5 ms                                                | 43.5 ms: 1.05x slower                                                     |
| sqlglot_optimize         | 36.8 ms                                                | 39.1 ms: 1.06x slower                                                     |
| gc_traversal             | 2.36 ms                                                | 2.94 ms: 1.24x slower                                                     |
| telco                    | 3.49 ms                                                | 4.47 ms: 1.28x slower                                                     |
| async_generators         | 231 ms                                                 | 298 ms: 1.29x slower                                                      |
| genshi_xml               | 33.8 ms                                                | 45.7 ms: 1.35x slower                                                     |
| create_gc_cycles         | 860 us                                                 | 1.33 ms: 1.55x slower                                                     |
| bench_mp_pool            | 37.4 ms                                                | 61.6 ms: 1.65x slower                                                     |
| python_startup           | 10.9 ms                                                | 18.0 ms: 1.65x slower                                                     |
| python_startup_no_site   | 7.91 ms                                                | 14.0 ms: 1.77x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.19x faster                                                              |

Benchmark hidden because not significant (3): 2to3, xml_etree_parse, scimark_sparse_mat_mult
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241024-3.14.0a1+-9698931-JIT/bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.201x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.42x