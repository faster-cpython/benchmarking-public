# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 0.61x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 160 ms: 1.20x faster                                                  |
| docutils       | 1.73 sec                                               | 1.45 sec: 1.19x faster                                                |
| html5lib       | 42.4 ms                                                | 30.1 ms: 1.41x faster                                                 |
| Geometric mean | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 193 ms: 2.01x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 250 ms: 1.90x faster                                                  |
| async_tree_io           | 980 ms                                                 | 597 ms: 1.64x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 458 ms: 1.42x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.4 ms: 1.57x faster                                                 |
| float          | 69.0 ms                                                | 48.7 ms: 1.42x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 67.5 ms: 1.41x faster                                                 |
| regex_dna      | 174 ms                                                 | 146 ms: 1.20x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 183 us: 1.53x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 142 us: 1.37x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.44 ms: 1.26x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.9 ms: 1.23x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.48 sec: 1.16x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 53.9 ms: 1.01x slower                                                 |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 73.9 ms: 1.02x slower                                                 |
| json_loads           | 16.4 us                                                | 17.2 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.6 ms: 1.53x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.5 ms: 1.71x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.62x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.10 ms: 1.39x faster                                                 |
| django_template | 26.4 ms                                                | 20.0 ms: 1.32x faster                                                 |
| genshi_text     | 17.3 ms                                                | 13.8 ms: 1.26x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.4 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 92.6 us: 3.49x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.15 ms: 2.29x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.6 us: 2.09x faster                                                 |
| raytrace                 | 301 ms                                                 | 149 ms: 2.02x faster                                                  |
| async_tree_none          | 388 ms                                                 | 193 ms: 2.01x faster                                                  |
| logging_silent           | 117 ns                                                 | 61.1 ns: 1.92x faster                                                 |
| go                       | 151 ms                                                 | 79.0 ms: 1.91x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 250 ms: 1.90x faster                                                  |
| deepcopy                 | 272 us                                                 | 145 us: 1.87x faster                                                  |
| chaos                    | 65.8 ms                                                | 35.8 ms: 1.84x faster                                                 |
| comprehensions           | 16.9 us                                                | 10.1 us: 1.68x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 741 us: 1.68x faster                                                  |
| richards_super           | 57.8 ms                                                | 35.1 ms: 1.65x faster                                                 |
| async_tree_io            | 980 ms                                                 | 597 ms: 1.64x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 411 ms: 1.60x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 903 us: 1.60x faster                                                  |
| generators               | 32.3 ms                                                | 20.4 ms: 1.59x faster                                                 |
| nbody                    | 93.0 ms                                                | 59.4 ms: 1.57x faster                                                 |
| richards                 | 48.7 ms                                                | 31.3 ms: 1.55x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.54x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 183 us: 1.53x faster                                                  |
| pylint                   | 277 ms                                                 | 181 ms: 1.53x faster                                                  |
| scimark_lu               | 103 ms                                                 | 67.8 ms: 1.52x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.09 ms: 1.51x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 43.3 ms: 1.51x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.10 us: 1.43x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 458 ms: 1.42x faster                                                  |
| float                    | 69.0 ms                                                | 48.7 ms: 1.42x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 453 ms: 1.41x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 50.9 ms: 1.41x faster                                                 |
| regex_compile            | 95.3 ms                                                | 67.5 ms: 1.41x faster                                                 |
| html5lib                 | 42.4 ms                                                | 30.1 ms: 1.41x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.4 ms: 1.41x faster                                                 |
| logging_format           | 4.83 us                                                | 3.44 us: 1.40x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 932 ms: 1.40x faster                                                  |
| mako                     | 9.87 ms                                                | 7.10 ms: 1.39x faster                                                 |
| scimark_sor              | 128 ms                                                 | 92.8 ms: 1.38x faster                                                 |
| pycparser                | 877 ms                                                 | 639 ms: 1.37x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 142 us: 1.37x faster                                                  |
| thrift                   | 572 us                                                 | 421 us: 1.36x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 69.0 ms: 1.34x faster                                                 |
| django_template          | 26.4 ms                                                | 20.0 ms: 1.32x faster                                                 |
| pyflate                  | 427 ms                                                 | 324 ms: 1.32x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 27.2 ms: 1.30x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.29x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.27x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.44 ms: 1.26x faster                                                 |
| genshi_text              | 17.3 ms                                                | 13.8 ms: 1.26x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.25x faster                                                |
| sympy_str                | 165 ms                                                 | 132 ms: 1.25x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.77 ms: 1.24x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 37.9 ms: 1.23x faster                                                 |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                                  |
| nqueens                  | 63.8 ms                                                | 53.3 ms: 1.20x faster                                                 |
| regex_dna                | 174 ms                                                 | 146 ms: 1.20x faster                                                  |
| 2to3                     | 192 ms                                                 | 160 ms: 1.20x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.45 sec: 1.19x faster                                                |
| sympy_expand             | 269 ms                                                 | 228 ms: 1.18x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 31.3 ms: 1.18x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 450 us: 1.17x faster                                                  |
| fannkuch                 | 303 ms                                                 | 261 ms: 1.16x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.48 sec: 1.16x faster                                                |
| mdp                      | 1.63 sec                                               | 1.43 sec: 1.14x faster                                                |
| sqlglot_normalize        | 190 ms                                                 | 168 ms: 1.13x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 30.4 ms: 1.11x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 74.2 ms: 1.05x faster                                                 |
| json                     | 3.08 ms                                                | 2.95 ms: 1.04x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                 |
| pathlib                  | 24.5 ms                                                | 24.1 ms: 1.02x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                  |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 53.9 ms: 1.01x slower                                                 |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.02x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 73.9 ms: 1.02x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 899 us: 1.05x slower                                                  |
| json_loads               | 16.4 us                                                | 17.2 us: 1.05x slower                                                 |
| coverage                 | 41.5 ms                                                | 44.5 ms: 1.07x slower                                                 |
| async_generators         | 231 ms                                                 | 282 ms: 1.22x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 48.9 ms: 1.31x slower                                                 |
| telco                    | 3.49 ms                                                | 4.75 ms: 1.36x slower                                                 |
| python_startup           | 10.9 ms                                                | 16.6 ms: 1.53x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.5 ms: 1.71x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (2): tornado_http, regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 0.61x