# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 0.71x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 161 ms: 1.19x faster                                                  |
| docutils       | 1.73 sec                                               | 1.45 sec: 1.19x faster                                                |
| html5lib       | 42.4 ms                                                | 30.2 ms: 1.40x faster                                                 |
| Geometric mean | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 193 ms: 2.01x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 250 ms: 1.89x faster                                                  |
| async_tree_io           | 980 ms                                                 | 597 ms: 1.64x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 458 ms: 1.42x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.72x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.3 ms: 1.57x faster                                                 |
| float          | 69.0 ms                                                | 48.9 ms: 1.41x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 67.4 ms: 1.41x faster                                                 |
| regex_dna      | 174 ms                                                 | 146 ms: 1.20x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.46 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 183 us: 1.54x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 143 us: 1.36x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.44 ms: 1.26x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.6 ms: 1.24x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.48 sec: 1.15x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 53.3 ms: 1.00x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 73.8 ms: 1.02x slower                                                 |
| json_loads           | 16.4 us                                                | 17.3 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.5 ms: 1.52x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.8 ms: 1.75x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.63x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.08 ms: 1.39x faster                                                 |
| django_template | 26.4 ms                                                | 19.9 ms: 1.33x faster                                                 |
| genshi_text     | 17.3 ms                                                | 13.8 ms: 1.26x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.3 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 91.2 us: 3.54x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.15 ms: 2.29x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.5 us: 2.10x faster                                                 |
| raytrace                 | 301 ms                                                 | 149 ms: 2.02x faster                                                  |
| async_tree_none          | 388 ms                                                 | 193 ms: 2.01x faster                                                  |
| logging_silent           | 117 ns                                                 | 61.2 ns: 1.92x faster                                                 |
| go                       | 151 ms                                                 | 79.2 ms: 1.90x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 250 ms: 1.89x faster                                                  |
| deepcopy                 | 272 us                                                 | 144 us: 1.89x faster                                                  |
| chaos                    | 65.8 ms                                                | 35.6 ms: 1.85x faster                                                 |
| comprehensions           | 16.9 us                                                | 9.95 us: 1.70x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 740 us: 1.68x faster                                                  |
| async_tree_io            | 980 ms                                                 | 597 ms: 1.64x faster                                                  |
| richards_super           | 57.8 ms                                                | 35.3 ms: 1.64x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 901 us: 1.60x faster                                                  |
| generators               | 32.3 ms                                                | 20.4 ms: 1.58x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 419 ms: 1.57x faster                                                  |
| nbody                    | 93.0 ms                                                | 59.3 ms: 1.57x faster                                                 |
| richards                 | 48.7 ms                                                | 31.5 ms: 1.55x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.54x faster                                                 |
| scimark_lu               | 103 ms                                                 | 66.7 ms: 1.54x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 183 us: 1.54x faster                                                  |
| pylint                   | 277 ms                                                 | 180 ms: 1.53x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.06 ms: 1.53x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 43.2 ms: 1.52x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.08 us: 1.44x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 50.4 ms: 1.42x faster                                                 |
| logging_format           | 4.83 us                                                | 3.39 us: 1.42x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 458 ms: 1.42x faster                                                  |
| regex_compile            | 95.3 ms                                                | 67.4 ms: 1.41x faster                                                 |
| float                    | 69.0 ms                                                | 48.9 ms: 1.41x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.3 ms: 1.41x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 455 ms: 1.41x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 928 ms: 1.41x faster                                                  |
| html5lib                 | 42.4 ms                                                | 30.2 ms: 1.40x faster                                                 |
| mako                     | 9.87 ms                                                | 7.08 ms: 1.39x faster                                                 |
| scimark_sor              | 128 ms                                                 | 93.0 ms: 1.38x faster                                                 |
| pycparser                | 877 ms                                                 | 641 ms: 1.37x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 143 us: 1.36x faster                                                  |
| thrift                   | 572 us                                                 | 427 us: 1.34x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 69.0 ms: 1.34x faster                                                 |
| pyflate                  | 427 ms                                                 | 320 ms: 1.33x faster                                                  |
| django_template          | 26.4 ms                                                | 19.9 ms: 1.33x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 27.0 ms: 1.31x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.29x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.28x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.44 ms: 1.26x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.26x faster                                                |
| genshi_text              | 17.3 ms                                                | 13.8 ms: 1.26x faster                                                 |
| sympy_str                | 165 ms                                                 | 132 ms: 1.25x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 37.6 ms: 1.24x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.78 ms: 1.23x faster                                                 |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                                  |
| nqueens                  | 63.8 ms                                                | 53.3 ms: 1.20x faster                                                 |
| regex_dna                | 174 ms                                                 | 146 ms: 1.20x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.45 sec: 1.19x faster                                                |
| 2to3                     | 192 ms                                                 | 161 ms: 1.19x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 31.1 ms: 1.18x faster                                                 |
| sympy_expand             | 269 ms                                                 | 228 ms: 1.18x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 450 us: 1.17x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.48 sec: 1.15x faster                                                |
| fannkuch                 | 303 ms                                                 | 263 ms: 1.15x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.43 sec: 1.14x faster                                                |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 30.3 ms: 1.12x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 72.1 ms: 1.08x faster                                                 |
| json                     | 3.08 ms                                                | 2.95 ms: 1.05x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.8 ms: 1.03x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 53.3 ms: 1.00x faster                                                 |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.46 ms: 1.00x slower                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 73.8 ms: 1.02x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 901 us: 1.05x slower                                                  |
| json_loads               | 16.4 us                                                | 17.3 us: 1.05x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.4 ms: 1.09x slower                                                 |
| async_generators         | 231 ms                                                 | 284 ms: 1.23x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 48.7 ms: 1.30x slower                                                 |
| telco                    | 3.49 ms                                                | 4.84 ms: 1.39x slower                                                 |
| python_startup           | 10.9 ms                                                | 16.5 ms: 1.52x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.8 ms: 1.75x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (2): tornado_http, xml_etree_parse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 0.71x