# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 7c66906
- commit date: 2024-07-03
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 192 ms                                                 | 205 ms: 1.07x slower                                  |
| docutils       | 1.73 sec                                               | 1.56 sec: 1.11x faster                                |
| html5lib       | 42.4 ms                                                | 31.6 ms: 1.34x faster                                 |
| tornado_http   | 86.7 ms                                                | 66.6 ms: 1.30x faster                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 232 ms: 2.04x faster                                  |
| async_tree_none         | 388 ms                                                 | 193 ms: 2.01x faster                                  |
| async_tree_io           | 980 ms                                                 | 533 ms: 1.84x faster                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 453 ms: 1.43x faster                                  |
| Geometric mean          | (ref)                                                  | 1.81x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.6 ms: 1.53x faster                                 |
| float          | 69.0 ms                                                | 49.8 ms: 1.38x faster                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.4 ms: 1.39x faster                                 |
| regex_dna      | 174 ms                                                 | 151 ms: 1.16x faster                                  |
| regex_v8       | 17.1 ms                                                | 17.5 ms: 1.02x slower                                 |
| regex_effbot   | 2.46 ms                                                | 2.64 ms: 1.07x slower                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 182 us: 1.54x faster                                  |
| unpickle_pure_python | 194 us                                                 | 143 us: 1.36x faster                                  |
| json_dumps           | 8.11 ms                                                | 6.44 ms: 1.26x faster                                 |
| xml_etree_process    | 46.5 ms                                                | 37.8 ms: 1.23x faster                                 |
| tomli_loads          | 1.71 sec                                               | 1.47 sec: 1.16x faster                                |
| json_loads           | 16.4 us                                                | 17.3 us: 1.05x slower                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                          |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 35.4 ms: 3.25x slower                                 |
| python_startup_no_site | 7.91 ms                                                | 26.4 ms: 3.33x slower                                 |
| Geometric mean         | (ref)                                                  | 3.29x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.19 ms: 1.37x faster                                 |
| django_template | 26.4 ms                                                | 19.9 ms: 1.33x faster                                 |
| genshi_text     | 17.3 ms                                                | 13.9 ms: 1.25x faster                                 |
| genshi_xml      | 33.8 ms                                                | 30.3 ms: 1.12x faster                                 |
| Geometric mean  | (ref)                                                  | 1.26x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 91.1 us: 3.54x faster                                 |
| deltablue                | 4.91 ms                                                | 2.13 ms: 2.30x faster                                 |
| deepcopy_memo            | 34.7 us                                                | 17.0 us: 2.05x faster                                 |
| async_tree_memoization   | 474 ms                                                 | 232 ms: 2.04x faster                                  |
| async_tree_none          | 388 ms                                                 | 193 ms: 2.01x faster                                  |
| raytrace                 | 301 ms                                                 | 150 ms: 2.00x faster                                  |
| logging_silent           | 117 ns                                                 | 58.9 ns: 1.99x faster                                 |
| deepcopy                 | 272 us                                                 | 145 us: 1.87x faster                                  |
| async_tree_io            | 980 ms                                                 | 533 ms: 1.84x faster                                  |
| chaos                    | 65.8 ms                                                | 36.0 ms: 1.83x faster                                 |
| sqlglot_parse            | 1.24 ms                                                | 746 us: 1.67x faster                                  |
| richards_super           | 57.8 ms                                                | 34.9 ms: 1.66x faster                                 |
| pylint                   | 277 ms                                                 | 174 ms: 1.59x faster                                  |
| sqlglot_transpile        | 1.44 ms                                                | 907 us: 1.59x faster                                  |
| comprehensions           | 16.9 us                                                | 10.7 us: 1.58x faster                                 |
| asyncio_tcp              | 659 ms                                                 | 424 ms: 1.55x faster                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.55x faster                                 |
| pickle_pure_python       | 281 us                                                 | 182 us: 1.54x faster                                  |
| nbody                    | 93.0 ms                                                | 60.6 ms: 1.53x faster                                 |
| richards                 | 48.7 ms                                                | 31.8 ms: 1.53x faster                                 |
| hexiom                   | 6.19 ms                                                | 4.09 ms: 1.51x faster                                 |
| go                       | 151 ms                                                 | 100 ms: 1.51x faster                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 43.7 ms: 1.50x faster                                 |
| scimark_lu               | 103 ms                                                 | 70.6 ms: 1.46x faster                                 |
| logging_simple           | 4.45 us                                                | 3.10 us: 1.44x faster                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 453 ms: 1.43x faster                                  |
| crypto_pyaes             | 71.8 ms                                                | 50.5 ms: 1.42x faster                                 |
| logging_format           | 4.83 us                                                | 3.41 us: 1.42x faster                                 |
| generators               | 32.3 ms                                                | 23.0 ms: 1.41x faster                                 |
| spectral_norm            | 94.8 ms                                                | 67.7 ms: 1.40x faster                                 |
| regex_compile            | 95.3 ms                                                | 68.4 ms: 1.39x faster                                 |
| float                    | 69.0 ms                                                | 49.8 ms: 1.38x faster                                 |
| mako                     | 9.87 ms                                                | 7.19 ms: 1.37x faster                                 |
| pycparser                | 877 ms                                                 | 640 ms: 1.37x faster                                  |
| pprint_pformat           | 1.30 sec                                               | 952 ms: 1.37x faster                                  |
| pprint_safe_repr         | 641 ms                                                 | 468 ms: 1.37x faster                                  |
| unpickle_pure_python     | 194 us                                                 | 143 us: 1.36x faster                                  |
| html5lib                 | 42.4 ms                                                | 31.6 ms: 1.34x faster                                 |
| scimark_sor              | 128 ms                                                 | 96.3 ms: 1.33x faster                                 |
| django_template          | 26.4 ms                                                | 19.9 ms: 1.33x faster                                 |
| thrift                   | 572 us                                                 | 433 us: 1.32x faster                                  |
| pyflate                  | 427 ms                                                 | 323 ms: 1.32x faster                                  |
| sympy_sum                | 92.2 ms                                                | 70.7 ms: 1.30x faster                                 |
| tornado_http             | 86.7 ms                                                | 66.6 ms: 1.30x faster                                 |
| coroutines               | 20.7 ms                                                | 16.2 ms: 1.27x faster                                 |
| json_dumps               | 8.11 ms                                                | 6.44 ms: 1.26x faster                                 |
| sympy_integrate          | 13.1 ms                                                | 10.5 ms: 1.25x faster                                 |
| genshi_text              | 17.3 ms                                                | 13.9 ms: 1.25x faster                                 |
| sympy_str                | 165 ms                                                 | 134 ms: 1.23x faster                                  |
| xml_etree_process        | 46.5 ms                                                | 37.8 ms: 1.23x faster                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.31 sec: 1.22x faster                                |
| scimark_fft              | 224 ms                                                 | 189 ms: 1.19x faster                                  |
| nqueens                  | 63.8 ms                                                | 54.0 ms: 1.18x faster                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.90 ms: 1.18x faster                                 |
| sqlglot_optimize         | 36.8 ms                                                | 31.3 ms: 1.17x faster                                 |
| sympy_expand             | 269 ms                                                 | 231 ms: 1.16x faster                                  |
| tomli_loads              | 1.71 sec                                               | 1.47 sec: 1.16x faster                                |
| bench_thread_pool        | 527 us                                                 | 455 us: 1.16x faster                                  |
| regex_dna                | 174 ms                                                 | 151 ms: 1.16x faster                                  |
| mdp                      | 1.63 sec                                               | 1.43 sec: 1.14x faster                                |
| fannkuch                 | 303 ms                                                 | 266 ms: 1.14x faster                                  |
| dask                     | 253 ms                                                 | 223 ms: 1.13x faster                                  |
| sqlglot_normalize        | 190 ms                                                 | 169 ms: 1.13x faster                                  |
| genshi_xml               | 33.8 ms                                                | 30.3 ms: 1.12x faster                                 |
| docutils                 | 1.73 sec                                               | 1.56 sec: 1.11x faster                                |
| meteor_contest           | 77.7 ms                                                | 71.6 ms: 1.09x faster                                 |
| pathlib                  | 24.5 ms                                                | 23.5 ms: 1.04x faster                                 |
| json                     | 3.08 ms                                                | 2.98 ms: 1.03x faster                                 |
| regex_v8                 | 17.1 ms                                                | 17.5 ms: 1.02x slower                                 |
| create_gc_cycles         | 860 us                                                 | 891 us: 1.04x slower                                  |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                 |
| json_loads               | 16.4 us                                                | 17.3 us: 1.05x slower                                 |
| regex_effbot             | 2.46 ms                                                | 2.64 ms: 1.07x slower                                 |
| 2to3                     | 192 ms                                                 | 205 ms: 1.07x slower                                  |
| coverage                 | 41.5 ms                                                | 44.8 ms: 1.08x slower                                 |
| async_generators         | 231 ms                                                 | 282 ms: 1.22x slower                                  |
| telco                    | 3.49 ms                                                | 4.60 ms: 1.32x slower                                 |
| bench_mp_pool            | 37.4 ms                                                | 85.9 ms: 2.30x slower                                 |
| python_startup           | 10.9 ms                                                | 35.4 ms: 3.25x slower                                 |
| python_startup_no_site   | 7.91 ms                                                | 26.4 ms: 3.33x slower                                 |
| Geometric mean           | (ref)                                                  | 1.26x faster                                          |

Benchmark hidden because not significant (5): xml_etree_parse, asyncio_websockets, pidigits, xml_etree_generate, xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240703-3.14.0a0-7c66906/bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.17x