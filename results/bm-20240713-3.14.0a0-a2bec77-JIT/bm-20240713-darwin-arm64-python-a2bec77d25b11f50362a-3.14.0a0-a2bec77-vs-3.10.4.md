# Results vs. 3.10.4

- fork: python
- ref: a2bec77d25b11f50362a
- machine: darwin-arm64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 172 ms: 1.12x faster                                                  |
| docutils       | 1.73 sec                                               | 1.52 sec: 1.14x faster                                                |
| html5lib       | 42.4 ms                                                | 32.7 ms: 1.30x faster                                                 |
| tornado_http   | 86.7 ms                                                | 67.3 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 233 ms: 2.03x faster                                                  |
| async_tree_none         | 388 ms                                                 | 193 ms: 2.01x faster                                                  |
| async_tree_io           | 980 ms                                                 | 527 ms: 1.86x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 453 ms: 1.43x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.82x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 64.2 ms: 1.45x faster                                                 |
| float          | 69.0 ms                                                | 47.8 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 73.7 ms: 1.29x faster                                                 |
| regex_dna      | 174 ms                                                 | 153 ms: 1.14x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.59 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 175 us: 1.60x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 133 us: 1.46x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.26 sec: 1.35x faster                                                |
| json_dumps           | 8.11 ms                                                | 6.27 ms: 1.29x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 36.4 ms: 1.28x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 71.4 ms: 1.01x faster                                                 |
| json_loads           | 16.4 us                                                | 17.3 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.4 ms: 1.42x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 12.8 ms: 1.62x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.51x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.51 ms: 1.52x faster                                                 |
| django_template | 26.4 ms                                                | 21.4 ms: 1.23x faster                                                 |
| genshi_text     | 17.3 ms                                                | 16.3 ms: 1.07x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 40.0 ms: 1.18x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 94.6 us: 3.41x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.33 ms: 2.11x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.8 us: 2.06x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 233 ms: 2.03x faster                                                  |
| async_tree_none          | 388 ms                                                 | 193 ms: 2.01x faster                                                  |
| logging_silent           | 117 ns                                                 | 61.5 ns: 1.91x faster                                                 |
| async_tree_io            | 980 ms                                                 | 527 ms: 1.86x faster                                                  |
| raytrace                 | 301 ms                                                 | 165 ms: 1.82x faster                                                  |
| deepcopy                 | 272 us                                                 | 153 us: 1.77x faster                                                  |
| chaos                    | 65.8 ms                                                | 39.3 ms: 1.67x faster                                                 |
| richards_super           | 57.8 ms                                                | 35.2 ms: 1.64x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 407 ms: 1.62x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 175 us: 1.60x faster                                                  |
| richards                 | 48.7 ms                                                | 31.5 ms: 1.54x faster                                                 |
| pylint                   | 277 ms                                                 | 180 ms: 1.54x faster                                                  |
| mako                     | 9.87 ms                                                | 6.51 ms: 1.52x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.56 us: 1.49x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 834 us: 1.49x faster                                                  |
| go                       | 151 ms                                                 | 101 ms: 1.49x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 44.1 ms: 1.49x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 133 us: 1.46x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.07 us: 1.45x faster                                                 |
| nbody                    | 93.0 ms                                                | 64.2 ms: 1.45x faster                                                 |
| float                    | 69.0 ms                                                | 47.8 ms: 1.44x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.00 ms: 1.44x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 453 ms: 1.43x faster                                                  |
| logging_format           | 4.83 us                                                | 3.39 us: 1.43x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.42 ms: 1.40x faster                                                 |
| generators               | 32.3 ms                                                | 23.2 ms: 1.39x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 68.8 ms: 1.38x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 52.2 ms: 1.38x faster                                                 |
| comprehensions           | 16.9 us                                                | 12.3 us: 1.37x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.26 sec: 1.35x faster                                                |
| pyflate                  | 427 ms                                                 | 317 ms: 1.34x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 480 ms: 1.34x faster                                                  |
| thrift                   | 572 us                                                 | 432 us: 1.32x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 988 ms: 1.32x faster                                                  |
| html5lib                 | 42.4 ms                                                | 32.7 ms: 1.30x faster                                                 |
| pycparser                | 877 ms                                                 | 676 ms: 1.30x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.27 ms: 1.29x faster                                                 |
| regex_compile            | 95.3 ms                                                | 73.7 ms: 1.29x faster                                                 |
| tornado_http             | 86.7 ms                                                | 67.3 ms: 1.29x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 36.4 ms: 1.28x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.2 ms: 1.28x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 72.9 ms: 1.27x faster                                                 |
| scimark_sor              | 128 ms                                                 | 102 ms: 1.26x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.25x faster                                                |
| scimark_lu               | 103 ms                                                 | 82.8 ms: 1.24x faster                                                 |
| django_template          | 26.4 ms                                                | 21.4 ms: 1.23x faster                                                 |
| fannkuch                 | 303 ms                                                 | 247 ms: 1.23x faster                                                  |
| sympy_str                | 165 ms                                                 | 139 ms: 1.19x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 11.0 ms: 1.19x faster                                                 |
| scimark_fft              | 224 ms                                                 | 191 ms: 1.17x faster                                                  |
| regex_dna                | 174 ms                                                 | 153 ms: 1.14x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.52 sec: 1.14x faster                                                |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.03 ms: 1.13x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.45 sec: 1.13x faster                                                |
| dask                     | 253 ms                                                 | 225 ms: 1.12x faster                                                  |
| sympy_expand             | 269 ms                                                 | 241 ms: 1.12x faster                                                  |
| 2to3                     | 192 ms                                                 | 172 ms: 1.12x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 33.2 ms: 1.11x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 476 us: 1.11x faster                                                  |
| nqueens                  | 63.8 ms                                                | 57.8 ms: 1.10x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 71.9 ms: 1.08x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 176 ms: 1.08x faster                                                  |
| genshi_text              | 17.3 ms                                                | 16.3 ms: 1.07x faster                                                 |
| json                     | 3.08 ms                                                | 2.93 ms: 1.05x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.8 ms: 1.03x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 71.4 ms: 1.01x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 905 us: 1.05x slower                                                  |
| json_loads               | 16.4 us                                                | 17.3 us: 1.05x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.59 ms: 1.06x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.7 ms: 1.10x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.61 ms: 1.10x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 40.0 ms: 1.18x slower                                                 |
| async_generators         | 231 ms                                                 | 293 ms: 1.27x slower                                                  |
| telco                    | 3.49 ms                                                | 4.56 ms: 1.31x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 50.2 ms: 1.34x slower                                                 |
| python_startup           | 10.9 ms                                                | 15.4 ms: 1.42x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 12.8 ms: 1.62x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.26x faster                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, xml_etree_generate, pidigits
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.30x