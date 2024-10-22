# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 0.74x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 162 ms: 1.18x faster                                                  |
| docutils       | 1.73 sec                                               | 1.45 sec: 1.19x faster                                                |
| html5lib       | 42.4 ms                                                | 30.1 ms: 1.41x faster                                                 |
| Geometric mean | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 193 ms: 2.02x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 250 ms: 1.89x faster                                                  |
| async_tree_io           | 980 ms                                                 | 595 ms: 1.65x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 458 ms: 1.42x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.5 ms: 1.56x faster                                                 |
| float          | 69.0 ms                                                | 48.7 ms: 1.42x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 67.8 ms: 1.41x faster                                                 |
| regex_dna      | 174 ms                                                 | 147 ms: 1.19x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.47 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 183 us: 1.53x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 142 us: 1.37x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.43 ms: 1.26x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.8 ms: 1.23x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.47 sec: 1.16x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 109 ms: 1.02x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 74.1 ms: 1.03x slower                                                 |
| json_loads           | 16.4 us                                                | 17.3 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.6 ms: 1.53x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.7 ms: 1.73x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.63x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.94 ms: 1.42x faster                                                 |
| django_template | 26.4 ms                                                | 19.6 ms: 1.34x faster                                                 |
| genshi_text     | 17.3 ms                                                | 13.9 ms: 1.25x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.3 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 91.6 us: 3.53x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.15 ms: 2.29x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.5 us: 2.10x faster                                                 |
| raytrace                 | 301 ms                                                 | 149 ms: 2.03x faster                                                  |
| async_tree_none          | 388 ms                                                 | 193 ms: 2.02x faster                                                  |
| logging_silent           | 117 ns                                                 | 61.3 ns: 1.91x faster                                                 |
| go                       | 151 ms                                                 | 79.2 ms: 1.90x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 250 ms: 1.89x faster                                                  |
| deepcopy                 | 272 us                                                 | 144 us: 1.89x faster                                                  |
| chaos                    | 65.8 ms                                                | 35.7 ms: 1.84x faster                                                 |
| comprehensions           | 16.9 us                                                | 9.96 us: 1.70x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 741 us: 1.68x faster                                                  |
| richards_super           | 57.8 ms                                                | 35.1 ms: 1.65x faster                                                 |
| async_tree_io            | 980 ms                                                 | 595 ms: 1.65x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 902 us: 1.60x faster                                                  |
| generators               | 32.3 ms                                                | 20.4 ms: 1.58x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 418 ms: 1.58x faster                                                  |
| nbody                    | 93.0 ms                                                | 59.5 ms: 1.56x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.50 us: 1.55x faster                                                 |
| richards                 | 48.7 ms                                                | 31.4 ms: 1.55x faster                                                 |
| scimark_lu               | 103 ms                                                 | 66.7 ms: 1.54x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 183 us: 1.53x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.07 ms: 1.52x faster                                                 |
| pylint                   | 277 ms                                                 | 182 ms: 1.52x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 43.2 ms: 1.52x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.09 us: 1.44x faster                                                 |
| mako                     | 9.87 ms                                                | 6.94 ms: 1.42x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 450 ms: 1.42x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 50.6 ms: 1.42x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 458 ms: 1.42x faster                                                  |
| float                    | 69.0 ms                                                | 48.7 ms: 1.42x faster                                                 |
| logging_format           | 4.83 us                                                | 3.41 us: 1.42x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 922 ms: 1.41x faster                                                  |
| html5lib                 | 42.4 ms                                                | 30.1 ms: 1.41x faster                                                 |
| regex_compile            | 95.3 ms                                                | 67.8 ms: 1.41x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.5 ms: 1.40x faster                                                 |
| scimark_sor              | 128 ms                                                 | 93.1 ms: 1.38x faster                                                 |
| pycparser                | 877 ms                                                 | 641 ms: 1.37x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 142 us: 1.37x faster                                                  |
| thrift                   | 572 us                                                 | 422 us: 1.36x faster                                                  |
| django_template          | 26.4 ms                                                | 19.6 ms: 1.34x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 69.1 ms: 1.33x faster                                                 |
| pyflate                  | 427 ms                                                 | 321 ms: 1.33x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 27.0 ms: 1.31x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.27x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.27 sec: 1.26x faster                                                |
| json_dumps               | 8.11 ms                                                | 6.43 ms: 1.26x faster                                                 |
| sympy_str                | 165 ms                                                 | 131 ms: 1.26x faster                                                  |
| genshi_text              | 17.3 ms                                                | 13.9 ms: 1.25x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.8 ms: 1.23x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 37.8 ms: 1.23x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.79 ms: 1.23x faster                                                 |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.21x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.45 sec: 1.19x faster                                                |
| nqueens                  | 63.8 ms                                                | 53.6 ms: 1.19x faster                                                 |
| regex_dna                | 174 ms                                                 | 147 ms: 1.19x faster                                                  |
| sympy_expand             | 269 ms                                                 | 227 ms: 1.19x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 31.2 ms: 1.18x faster                                                 |
| 2to3                     | 192 ms                                                 | 162 ms: 1.18x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 451 us: 1.17x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.47 sec: 1.16x faster                                                |
| fannkuch                 | 303 ms                                                 | 263 ms: 1.15x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.43 sec: 1.14x faster                                                |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 30.3 ms: 1.12x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 72.4 ms: 1.07x faster                                                 |
| json                     | 3.08 ms                                                | 2.96 ms: 1.04x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                 |
| pathlib                  | 24.5 ms                                                | 24.0 ms: 1.02x faster                                                 |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.47 ms: 1.01x slower                                                 |
| xml_etree_parse          | 108 ms                                                 | 109 ms: 1.02x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 74.1 ms: 1.03x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 905 us: 1.05x slower                                                  |
| json_loads               | 16.4 us                                                | 17.3 us: 1.05x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.0 ms: 1.09x slower                                                 |
| async_generators         | 231 ms                                                 | 281 ms: 1.21x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 48.9 ms: 1.31x slower                                                 |
| telco                    | 3.49 ms                                                | 4.84 ms: 1.39x slower                                                 |
| python_startup           | 10.9 ms                                                | 16.6 ms: 1.53x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.7 ms: 1.73x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (3): tornado_http, asyncio_websockets, xml_etree_generate
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 0.74x