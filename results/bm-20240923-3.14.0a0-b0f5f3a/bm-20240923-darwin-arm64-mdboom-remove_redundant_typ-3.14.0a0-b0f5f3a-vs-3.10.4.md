# Results vs. 3.10.4

- fork: mdboom
- ref: remove_redundant_typ
- machine: darwin-arm64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 0.74x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 162 ms: 1.19x faster                                                  |
| docutils       | 1.73 sec                                               | 1.45 sec: 1.20x faster                                                |
| html5lib       | 42.4 ms                                                | 30.0 ms: 1.41x faster                                                 |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 199 ms: 1.96x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 246 ms: 1.92x faster                                                  |
| async_tree_io           | 980 ms                                                 | 582 ms: 1.68x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 459 ms: 1.42x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.0 ms: 1.55x faster                                                 |
| float          | 69.0 ms                                                | 48.5 ms: 1.42x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 67.0 ms: 1.42x faster                                                 |
| regex_dna      | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 180 us: 1.56x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 140 us: 1.39x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.30 ms: 1.29x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.5 ms: 1.24x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.47 sec: 1.16x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 52.9 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 73.7 ms: 1.02x slower                                                 |
| json_loads           | 16.4 us                                                | 16.8 us: 1.02x slower                                                 |
| unpickle             | 8.80 us                                                | 9.07 us: 1.03x slower                                                 |
| pickle               | 6.97 us                                                | 7.34 us: 1.05x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.07x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.90 us: 1.08x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.96 us: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.0 ms: 1.47x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.1 ms: 1.65x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.56x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.12 ms: 1.39x faster                                                 |
| django_template | 26.4 ms                                                | 20.0 ms: 1.32x faster                                                 |
| genshi_text     | 17.3 ms                                                | 13.8 ms: 1.26x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.3 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 93.6 us: 3.45x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.13 ms: 2.31x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.6 us: 2.09x faster                                                 |
| raytrace                 | 301 ms                                                 | 149 ms: 2.02x faster                                                  |
| async_tree_none          | 388 ms                                                 | 199 ms: 1.96x faster                                                  |
| logging_silent           | 117 ns                                                 | 60.8 ns: 1.93x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 246 ms: 1.92x faster                                                  |
| go                       | 151 ms                                                 | 79.2 ms: 1.90x faster                                                 |
| deepcopy                 | 272 us                                                 | 144 us: 1.89x faster                                                  |
| chaos                    | 65.8 ms                                                | 35.6 ms: 1.85x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 736 us: 1.69x faster                                                  |
| async_tree_io            | 980 ms                                                 | 582 ms: 1.68x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 898 us: 1.61x faster                                                  |
| richards_super           | 57.8 ms                                                | 36.2 ms: 1.60x faster                                                 |
| scimark_lu               | 103 ms                                                 | 64.6 ms: 1.59x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 416 ms: 1.58x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 180 us: 1.56x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.50 us: 1.56x faster                                                 |
| comprehensions           | 16.9 us                                                | 10.9 us: 1.55x faster                                                 |
| pylint                   | 277 ms                                                 | 178 ms: 1.55x faster                                                  |
| nbody                    | 93.0 ms                                                | 60.0 ms: 1.55x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 42.4 ms: 1.55x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.04 ms: 1.53x faster                                                 |
| generators               | 32.3 ms                                                | 21.1 ms: 1.53x faster                                                 |
| richards                 | 48.7 ms                                                | 32.4 ms: 1.50x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.00 us: 1.48x faster                                                 |
| unpack_sequence          | 39.0 ns                                                | 26.4 ns: 1.48x faster                                                 |
| logging_format           | 4.83 us                                                | 3.28 us: 1.47x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 50.0 ms: 1.44x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 66.0 ms: 1.44x faster                                                 |
| regex_compile            | 95.3 ms                                                | 67.0 ms: 1.42x faster                                                 |
| float                    | 69.0 ms                                                | 48.5 ms: 1.42x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 459 ms: 1.42x faster                                                  |
| html5lib                 | 42.4 ms                                                | 30.0 ms: 1.41x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 930 ms: 1.40x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 457 ms: 1.40x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 140 us: 1.39x faster                                                  |
| mako                     | 9.87 ms                                                | 7.12 ms: 1.39x faster                                                 |
| scimark_sor              | 128 ms                                                 | 92.7 ms: 1.38x faster                                                 |
| pycparser                | 877 ms                                                 | 637 ms: 1.38x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 68.7 ms: 1.34x faster                                                 |
| thrift                   | 572 us                                                 | 426 us: 1.34x faster                                                  |
| pyflate                  | 427 ms                                                 | 320 ms: 1.33x faster                                                  |
| django_template          | 26.4 ms                                                | 20.0 ms: 1.32x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 27.3 ms: 1.29x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.0 ms: 1.29x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.30 ms: 1.29x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.28x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.70 ms: 1.27x faster                                                 |
| genshi_text              | 17.3 ms                                                | 13.8 ms: 1.26x faster                                                 |
| scimark_fft              | 224 ms                                                 | 179 ms: 1.25x faster                                                  |
| sympy_str                | 165 ms                                                 | 132 ms: 1.25x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.25x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 37.5 ms: 1.24x faster                                                 |
| regex_dna                | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| nqueens                  | 63.8 ms                                                | 53.2 ms: 1.20x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.45 sec: 1.20x faster                                                |
| 2to3                     | 192 ms                                                 | 162 ms: 1.19x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 31.1 ms: 1.18x faster                                                 |
| sympy_expand             | 269 ms                                                 | 227 ms: 1.18x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 448 us: 1.18x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.47 sec: 1.16x faster                                                |
| fannkuch                 | 303 ms                                                 | 261 ms: 1.16x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.44 sec: 1.13x faster                                                |
| genshi_xml               | 33.8 ms                                                | 30.3 ms: 1.12x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 71.3 ms: 1.09x faster                                                 |
| json                     | 3.08 ms                                                | 2.91 ms: 1.06x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.5 ms: 1.04x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.04x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 52.9 ms: 1.01x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 73.7 ms: 1.02x slower                                                 |
| json_loads               | 16.4 us                                                | 16.8 us: 1.02x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.07 us: 1.03x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 892 us: 1.04x slower                                                  |
| pickle                   | 6.97 us                                                | 7.34 us: 1.05x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.05x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.07x slower                                                 |
| coverage                 | 41.5 ms                                                | 44.4 ms: 1.07x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.90 us: 1.08x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.96 us: 1.08x slower                                                 |
| async_generators         | 231 ms                                                 | 278 ms: 1.20x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 48.0 ms: 1.28x slower                                                 |
| telco                    | 3.49 ms                                                | 4.81 ms: 1.38x slower                                                 |
| python_startup           | 10.9 ms                                                | 16.0 ms: 1.47x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.1 ms: 1.65x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                          |

Benchmark hidden because not significant (3): tornado_http, regex_effbot, xml_etree_parse
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 0.74x