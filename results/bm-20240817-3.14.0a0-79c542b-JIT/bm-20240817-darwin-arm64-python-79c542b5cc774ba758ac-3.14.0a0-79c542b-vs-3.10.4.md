# Results vs. 3.10.4

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: darwin-arm64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 0.85x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 179 ms: 1.07x faster                                                  |
| docutils       | 1.73 sec                                               | 1.62 sec: 1.07x faster                                                |
| html5lib       | 42.4 ms                                                | 34.5 ms: 1.23x faster                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 197 ms: 1.97x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 242 ms: 1.96x faster                                                  |
| async_tree_io           | 980 ms                                                 | 543 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 456 ms: 1.42x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.77x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.6 ms: 1.48x faster                                                 |
| nbody          | 93.0 ms                                                | 63.8 ms: 1.46x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 74.8 ms: 1.27x faster                                                 |
| regex_dna      | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.9 ms: 1.02x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.46 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 179 us: 1.57x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 134 us: 1.45x faster                                                  |
| xml_etree_process    | 46.5 ms                                                | 34.4 ms: 1.35x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.26 sec: 1.35x faster                                                |
| json_dumps           | 8.11 ms                                                | 6.50 ms: 1.25x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 50.3 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 71.7 ms: 1.01x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 109 ms: 1.01x slower                                                  |
| json_loads           | 16.4 us                                                | 17.2 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.3 ms: 1.32x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 11.6 ms: 1.46x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.39x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.50 ms: 1.52x faster                                                 |
| django_template | 26.4 ms                                                | 23.0 ms: 1.15x faster                                                 |
| genshi_text     | 17.3 ms                                                | 17.0 ms: 1.02x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 42.1 ms: 1.25x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 95.8 us: 3.37x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.2 us: 2.15x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.32 ms: 2.12x faster                                                 |
| async_tree_none          | 388 ms                                                 | 197 ms: 1.97x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 242 ms: 1.96x faster                                                  |
| logging_silent           | 117 ns                                                 | 62.1 ns: 1.89x faster                                                 |
| raytrace                 | 301 ms                                                 | 164 ms: 1.84x faster                                                  |
| async_tree_io            | 980 ms                                                 | 543 ms: 1.80x faster                                                  |
| deepcopy                 | 272 us                                                 | 155 us: 1.75x faster                                                  |
| chaos                    | 65.8 ms                                                | 40.1 ms: 1.64x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 179 us: 1.57x faster                                                  |
| scimark_lu               | 103 ms                                                 | 65.6 ms: 1.57x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.55x faster                                                 |
| mako                     | 9.87 ms                                                | 6.50 ms: 1.52x faster                                                 |
| go                       | 151 ms                                                 | 102 ms: 1.48x faster                                                  |
| float                    | 69.0 ms                                                | 46.6 ms: 1.48x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.02 us: 1.47x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 448 ms: 1.47x faster                                                  |
| nbody                    | 93.0 ms                                                | 63.8 ms: 1.46x faster                                                 |
| scimark_sor              | 128 ms                                                 | 88.0 ms: 1.46x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 856 us: 1.45x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 134 us: 1.45x faster                                                  |
| logging_format           | 4.83 us                                                | 3.33 us: 1.45x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 456 ms: 1.42x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 52.1 ms: 1.38x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.05 ms: 1.37x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 48.0 ms: 1.37x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 69.7 ms: 1.36x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 34.4 ms: 1.35x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.26 sec: 1.35x faster                                                |
| pylint                   | 277 ms                                                 | 205 ms: 1.35x faster                                                  |
| comprehensions           | 16.9 us                                                | 12.7 us: 1.34x faster                                                 |
| generators               | 32.3 ms                                                | 24.5 ms: 1.32x faster                                                 |
| thrift                   | 572 us                                                 | 434 us: 1.32x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.72 ms: 1.31x faster                                                 |
| pyflate                  | 427 ms                                                 | 327 ms: 1.31x faster                                                  |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.29x faster                                                 |
| regex_compile            | 95.3 ms                                                | 74.8 ms: 1.27x faster                                                 |
| pycparser                | 877 ms                                                 | 695 ms: 1.26x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 28.2 ms: 1.25x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 512 ms: 1.25x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.50 ms: 1.25x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 1.05 sec: 1.24x faster                                                |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                                |
| html5lib                 | 42.4 ms                                                | 34.5 ms: 1.23x faster                                                 |
| regex_dna                | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| richards_super           | 57.8 ms                                                | 48.1 ms: 1.20x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 77.3 ms: 1.19x faster                                                 |
| scimark_fft              | 224 ms                                                 | 194 ms: 1.16x faster                                                  |
| django_template          | 26.4 ms                                                | 23.0 ms: 1.15x faster                                                 |
| sympy_str                | 165 ms                                                 | 147 ms: 1.13x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 469 us: 1.13x faster                                                  |
| fannkuch                 | 303 ms                                                 | 269 ms: 1.12x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.45 sec: 1.12x faster                                                |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.08 ms: 1.11x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 11.9 ms: 1.10x faster                                                 |
| nqueens                  | 63.8 ms                                                | 59.2 ms: 1.08x faster                                                 |
| 2to3                     | 192 ms                                                 | 179 ms: 1.07x faster                                                  |
| sympy_expand             | 269 ms                                                 | 252 ms: 1.07x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.62 sec: 1.07x faster                                                |
| xml_etree_generate       | 53.5 ms                                                | 50.3 ms: 1.06x faster                                                 |
| richards                 | 48.7 ms                                                | 45.9 ms: 1.06x faster                                                 |
| json                     | 3.08 ms                                                | 2.92 ms: 1.05x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.5 ms: 1.04x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 74.6 ms: 1.04x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 185 ms: 1.03x faster                                                  |
| genshi_text              | 17.3 ms                                                | 17.0 ms: 1.02x faster                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 36.0 ms: 1.02x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.9 ms: 1.02x faster                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 71.7 ms: 1.01x faster                                                 |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.46 ms: 1.00x slower                                                 |
| xml_etree_parse          | 108 ms                                                 | 109 ms: 1.01x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 893 us: 1.04x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| json_loads               | 16.4 us                                                | 17.2 us: 1.05x slower                                                 |
| coverage                 | 41.5 ms                                                | 44.6 ms: 1.07x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 42.1 ms: 1.25x slower                                                 |
| async_generators         | 231 ms                                                 | 297 ms: 1.28x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 49.1 ms: 1.31x slower                                                 |
| python_startup           | 10.9 ms                                                | 14.3 ms: 1.32x slower                                                 |
| telco                    | 3.49 ms                                                | 4.64 ms: 1.33x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 11.6 ms: 1.46x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                          |

Benchmark hidden because not significant (2): tornado_http, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 0.85x