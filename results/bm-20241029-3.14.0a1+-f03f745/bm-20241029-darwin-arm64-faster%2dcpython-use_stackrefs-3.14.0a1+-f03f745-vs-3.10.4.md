# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs
- machine: darwin-arm64
- commit hash: f03f745
- commit date: 2024-10-29
- overall geometric mean: 1.218x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 171 ms: 1.12x faster                                                      |
| docutils       | 1.73 sec                                               | 1.47 sec: 1.18x faster                                                    |
| html5lib       | 42.4 ms                                                | 33.5 ms: 1.26x faster                                                     |
| Geometric mean | (ref)                                                  | 1.14x faster                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 213 ms: 1.83x faster                                                      |
| async_tree_memoization  | 474 ms                                                 | 262 ms: 1.81x faster                                                      |
| async_tree_io           | 980 ms                                                 | 596 ms: 1.64x faster                                                      |
| async_tree_cpu_io_mixed | 649 ms                                                 | 469 ms: 1.38x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.66x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 64.9 ms: 1.43x faster                                                     |
| float          | 69.0 ms                                                | 51.4 ms: 1.34x faster                                                     |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.24x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 74.2 ms: 1.28x faster                                                     |
| regex_dna      | 174 ms                                                 | 140 ms: 1.24x faster                                                      |
| regex_v8       | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                     |
| regex_effbot   | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 209 us: 1.35x faster                                                      |
| unpickle_pure_python | 194 us                                                 | 167 us: 1.17x faster                                                      |
| xml_etree_process    | 46.5 ms                                                | 40.8 ms: 1.14x faster                                                     |
| json_dumps           | 8.11 ms                                                | 7.37 ms: 1.10x faster                                                     |
| tomli_loads          | 1.71 sec                                               | 1.64 sec: 1.04x faster                                                    |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.01x faster                                                      |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                                     |
| xml_etree_iterparse  | 72.1 ms                                                | 74.8 ms: 1.04x slower                                                     |
| xml_etree_generate   | 53.5 ms                                                | 58.6 ms: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.91 ms                                                | 12.4 ms: 1.57x slower                                                     |
| python_startup         | 10.9 ms                                                | 17.1 ms: 1.58x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.57x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.35 ms: 1.34x faster                                                     |
| django_template | 26.4 ms                                                | 21.5 ms: 1.23x faster                                                     |
| genshi_text     | 17.3 ms                                                | 15.8 ms: 1.10x faster                                                     |
| genshi_xml      | 33.8 ms                                                | 32.9 ms: 1.03x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.17x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 101 us: 3.21x faster                                                      |
| deepcopy_memo            | 34.7 us                                                | 17.8 us: 1.95x faster                                                     |
| deltablue                | 4.91 ms                                                | 2.53 ms: 1.94x faster                                                     |
| raytrace                 | 301 ms                                                 | 164 ms: 1.84x faster                                                      |
| async_tree_none          | 388 ms                                                 | 213 ms: 1.83x faster                                                      |
| async_tree_memoization   | 474 ms                                                 | 262 ms: 1.81x faster                                                      |
| deepcopy                 | 272 us                                                 | 155 us: 1.75x faster                                                      |
| logging_silent           | 117 ns                                                 | 69.0 ns: 1.70x faster                                                     |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                      |
| async_tree_io            | 980 ms                                                 | 596 ms: 1.64x faster                                                      |
| chaos                    | 65.8 ms                                                | 40.0 ms: 1.64x faster                                                     |
| sqlglot_parse            | 1.24 ms                                                | 792 us: 1.57x faster                                                      |
| go                       | 151 ms                                                 | 96.4 ms: 1.56x faster                                                     |
| comprehensions           | 16.9 us                                                | 11.2 us: 1.52x faster                                                     |
| sqlglot_transpile        | 1.44 ms                                                | 962 us: 1.50x faster                                                      |
| richards_super           | 57.8 ms                                                | 39.2 ms: 1.48x faster                                                     |
| pylint                   | 277 ms                                                 | 189 ms: 1.47x faster                                                      |
| nbody                    | 93.0 ms                                                | 64.9 ms: 1.43x faster                                                     |
| scimark_monte_carlo      | 65.6 ms                                                | 46.2 ms: 1.42x faster                                                     |
| generators               | 32.3 ms                                                | 22.8 ms: 1.42x faster                                                     |
| deepcopy_reduce          | 2.33 us                                                | 1.65 us: 1.41x faster                                                     |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 469 ms: 1.38x faster                                                      |
| richards                 | 48.7 ms                                                | 35.3 ms: 1.38x faster                                                     |
| scimark_lu               | 103 ms                                                 | 75.3 ms: 1.37x faster                                                     |
| pickle_pure_python       | 281 us                                                 | 209 us: 1.35x faster                                                      |
| mako                     | 9.87 ms                                                | 7.35 ms: 1.34x faster                                                     |
| float                    | 69.0 ms                                                | 51.4 ms: 1.34x faster                                                     |
| pprint_safe_repr         | 641 ms                                                 | 480 ms: 1.33x faster                                                      |
| pprint_pformat           | 1.30 sec                                               | 979 ms: 1.33x faster                                                      |
| hexiom                   | 6.19 ms                                                | 4.72 ms: 1.31x faster                                                     |
| thrift                   | 572 us                                                 | 442 us: 1.29x faster                                                      |
| logging_simple           | 4.45 us                                                | 3.44 us: 1.29x faster                                                     |
| pycparser                | 877 ms                                                 | 678 ms: 1.29x faster                                                      |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.88 ms: 1.29x faster                                                     |
| regex_compile            | 95.3 ms                                                | 74.2 ms: 1.28x faster                                                     |
| logging_format           | 4.83 us                                                | 3.78 us: 1.28x faster                                                     |
| html5lib                 | 42.4 ms                                                | 33.5 ms: 1.26x faster                                                     |
| sympy_sum                | 92.2 ms                                                | 73.2 ms: 1.26x faster                                                     |
| scimark_sor              | 128 ms                                                 | 103 ms: 1.24x faster                                                      |
| regex_dna                | 174 ms                                                 | 140 ms: 1.24x faster                                                      |
| sqlalchemy_declarative   | 73.3 ms                                                | 59.6 ms: 1.23x faster                                                     |
| pyflate                  | 427 ms                                                 | 347 ms: 1.23x faster                                                      |
| dulwich_log              | 35.3 ms                                                | 28.8 ms: 1.23x faster                                                     |
| crypto_pyaes             | 71.8 ms                                                | 58.6 ms: 1.23x faster                                                     |
| django_template          | 26.4 ms                                                | 21.5 ms: 1.23x faster                                                     |
| spectral_norm            | 94.8 ms                                                | 78.0 ms: 1.22x faster                                                     |
| docutils                 | 1.73 sec                                               | 1.47 sec: 1.18x faster                                                    |
| unpickle_pure_python     | 194 us                                                 | 167 us: 1.17x faster                                                      |
| sympy_str                | 165 ms                                                 | 143 ms: 1.16x faster                                                      |
| coroutines               | 20.7 ms                                                | 18.1 ms: 1.15x faster                                                     |
| sympy_integrate          | 13.1 ms                                                | 11.5 ms: 1.15x faster                                                     |
| xml_etree_process        | 46.5 ms                                                | 40.8 ms: 1.14x faster                                                     |
| 2to3                     | 192 ms                                                 | 171 ms: 1.12x faster                                                      |
| bench_thread_pool        | 527 us                                                 | 474 us: 1.11x faster                                                      |
| sympy_expand             | 269 ms                                                 | 242 ms: 1.11x faster                                                      |
| nqueens                  | 63.8 ms                                                | 57.6 ms: 1.11x faster                                                     |
| scimark_fft              | 224 ms                                                 | 203 ms: 1.10x faster                                                      |
| sqlglot_optimize         | 36.8 ms                                                | 33.3 ms: 1.10x faster                                                     |
| json_dumps               | 8.11 ms                                                | 7.37 ms: 1.10x faster                                                     |
| genshi_text              | 17.3 ms                                                | 15.8 ms: 1.10x faster                                                     |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.13 ms: 1.09x faster                                                     |
| mdp                      | 1.63 sec                                               | 1.50 sec: 1.08x faster                                                    |
| pathlib                  | 24.5 ms                                                | 22.8 ms: 1.08x faster                                                     |
| sqlglot_normalize        | 190 ms                                                 | 177 ms: 1.07x faster                                                      |
| meteor_contest           | 77.7 ms                                                | 72.8 ms: 1.07x faster                                                     |
| fannkuch                 | 303 ms                                                 | 283 ms: 1.07x faster                                                      |
| json                     | 3.08 ms                                                | 2.94 ms: 1.05x faster                                                     |
| tomli_loads              | 1.71 sec                                               | 1.64 sec: 1.04x faster                                                    |
| regex_v8                 | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                     |
| genshi_xml               | 33.8 ms                                                | 32.9 ms: 1.03x faster                                                     |
| xml_etree_parse          | 108 ms                                                 | 106 ms: 1.01x faster                                                      |
| regex_effbot             | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                     |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                      |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                                     |
| xml_etree_iterparse      | 72.1 ms                                                | 74.8 ms: 1.04x slower                                                     |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.05x slower                                                     |
| coverage                 | 41.5 ms                                                | 44.2 ms: 1.07x slower                                                     |
| xml_etree_generate       | 53.5 ms                                                | 58.6 ms: 1.10x slower                                                     |
| gc_traversal             | 2.36 ms                                                | 2.94 ms: 1.25x slower                                                     |
| async_generators         | 231 ms                                                 | 289 ms: 1.25x slower                                                      |
| telco                    | 3.49 ms                                                | 4.69 ms: 1.34x slower                                                     |
| create_gc_cycles         | 860 us                                                 | 1.33 ms: 1.54x slower                                                     |
| python_startup_no_site   | 7.91 ms                                                | 12.4 ms: 1.57x slower                                                     |
| python_startup           | 10.9 ms                                                | 17.1 ms: 1.58x slower                                                     |
| bench_mp_pool            | 37.4 ms                                                | 59.1 ms: 1.58x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.21x faster                                                              |

Benchmark hidden because not significant (1): tornado_http
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20241029-3.14.0a1+-f03f745/bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.218x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.32x