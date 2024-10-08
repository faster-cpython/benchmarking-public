# Results vs. 3.10.4

- fork: python
- ref: a2bec77d25b11f50362a
- machine: darwin-arm64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 161 ms: 1.19x faster                                                  |
| docutils       | 1.73 sec                                               | 1.46 sec: 1.19x faster                                                |
| html5lib       | 42.4 ms                                                | 31.6 ms: 1.34x faster                                                 |
| tornado_http   | 86.7 ms                                                | 66.9 ms: 1.30x faster                                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 232 ms: 2.04x faster                                                  |
| async_tree_none         | 388 ms                                                 | 194 ms: 2.01x faster                                                  |
| async_tree_io           | 980 ms                                                 | 534 ms: 1.84x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 454 ms: 1.43x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.81x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.6 ms: 1.54x faster                                                 |
| float          | 69.0 ms                                                | 50.1 ms: 1.38x faster                                                 |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.5 ms: 1.39x faster                                                 |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.59 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 181 us: 1.55x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 143 us: 1.36x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.40 ms: 1.27x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.9 ms: 1.23x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.49 sec: 1.15x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 53.8 ms: 1.01x slower                                                 |
| json_loads           | 16.4 us                                                | 17.2 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.6 ms: 1.44x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 12.7 ms: 1.61x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.52x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.14 ms: 1.38x faster                                                 |
| django_template | 26.4 ms                                                | 19.9 ms: 1.32x faster                                                 |
| genshi_text     | 17.3 ms                                                | 14.1 ms: 1.23x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.3 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.26x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 91.9 us: 3.51x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.11 ms: 2.33x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 232 ms: 2.04x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 17.0 us: 2.04x faster                                                 |
| async_tree_none          | 388 ms                                                 | 194 ms: 2.01x faster                                                  |
| raytrace                 | 301 ms                                                 | 151 ms: 2.00x faster                                                  |
| logging_silent           | 117 ns                                                 | 59.4 ns: 1.97x faster                                                 |
| deepcopy                 | 272 us                                                 | 145 us: 1.87x faster                                                  |
| async_tree_io            | 980 ms                                                 | 534 ms: 1.84x faster                                                  |
| chaos                    | 65.8 ms                                                | 36.1 ms: 1.82x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 746 us: 1.67x faster                                                  |
| richards_super           | 57.8 ms                                                | 34.8 ms: 1.66x faster                                                 |
| pylint                   | 277 ms                                                 | 172 ms: 1.61x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 412 ms: 1.60x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 906 us: 1.59x faster                                                  |
| comprehensions           | 16.9 us                                                | 10.7 us: 1.58x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.50 us: 1.56x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 181 us: 1.55x faster                                                  |
| richards                 | 48.7 ms                                                | 31.6 ms: 1.54x faster                                                 |
| nbody                    | 93.0 ms                                                | 60.6 ms: 1.54x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.08 ms: 1.52x faster                                                 |
| go                       | 151 ms                                                 | 100 ms: 1.51x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 43.7 ms: 1.50x faster                                                 |
| scimark_lu               | 103 ms                                                 | 70.8 ms: 1.45x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.10 us: 1.43x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 454 ms: 1.43x faster                                                  |
| logging_format           | 4.83 us                                                | 3.39 us: 1.42x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 50.5 ms: 1.42x faster                                                 |
| generators               | 32.3 ms                                                | 22.8 ms: 1.42x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 68.0 ms: 1.39x faster                                                 |
| regex_compile            | 95.3 ms                                                | 68.5 ms: 1.39x faster                                                 |
| mako                     | 9.87 ms                                                | 7.14 ms: 1.38x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 465 ms: 1.38x faster                                                  |
| float                    | 69.0 ms                                                | 50.1 ms: 1.38x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 948 ms: 1.38x faster                                                  |
| pycparser                | 877 ms                                                 | 639 ms: 1.37x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 143 us: 1.36x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.6 ms: 1.34x faster                                                 |
| scimark_sor              | 128 ms                                                 | 96.3 ms: 1.33x faster                                                 |
| pyflate                  | 427 ms                                                 | 322 ms: 1.32x faster                                                  |
| django_template          | 26.4 ms                                                | 19.9 ms: 1.32x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 70.6 ms: 1.31x faster                                                 |
| thrift                   | 572 us                                                 | 438 us: 1.31x faster                                                  |
| tornado_http             | 86.7 ms                                                | 66.9 ms: 1.30x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.3 ms: 1.27x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.40 ms: 1.27x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.5 ms: 1.26x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.25x faster                                                |
| genshi_text              | 17.3 ms                                                | 14.1 ms: 1.23x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 37.9 ms: 1.23x faster                                                 |
| sympy_str                | 165 ms                                                 | 135 ms: 1.22x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.46 sec: 1.19x faster                                                |
| 2to3                     | 192 ms                                                 | 161 ms: 1.19x faster                                                  |
| scimark_fft              | 224 ms                                                 | 189 ms: 1.19x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.91 ms: 1.18x faster                                                 |
| nqueens                  | 63.8 ms                                                | 54.2 ms: 1.18x faster                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 31.5 ms: 1.17x faster                                                 |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| sympy_expand             | 269 ms                                                 | 231 ms: 1.16x faster                                                  |
| fannkuch                 | 303 ms                                                 | 261 ms: 1.16x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 455 us: 1.16x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.42 sec: 1.15x faster                                                |
| tomli_loads              | 1.71 sec                                               | 1.49 sec: 1.15x faster                                                |
| dask                     | 253 ms                                                 | 221 ms: 1.14x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 169 ms: 1.13x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 30.3 ms: 1.11x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 71.2 ms: 1.09x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.5 ms: 1.04x faster                                                 |
| json                     | 3.08 ms                                                | 2.97 ms: 1.04x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 53.8 ms: 1.01x slower                                                 |
| regex_v8                 | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 900 us: 1.05x slower                                                  |
| json_loads               | 16.4 us                                                | 17.2 us: 1.05x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.59 ms: 1.05x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.3 ms: 1.09x slower                                                 |
| async_generators         | 231 ms                                                 | 283 ms: 1.22x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 48.4 ms: 1.29x slower                                                 |
| telco                    | 3.49 ms                                                | 4.62 ms: 1.33x slower                                                 |
| python_startup           | 10.9 ms                                                | 15.6 ms: 1.44x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 12.7 ms: 1.61x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, pidigits, xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.18x