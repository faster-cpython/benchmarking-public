# Results vs. 3.10.4

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: darwin-arm64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 174 ms: 1.10x faster                                                  |
| docutils       | 1.73 sec                                               | 1.54 sec: 1.13x faster                                                |
| html5lib       | 42.4 ms                                                | 30.9 ms: 1.37x faster                                                 |
| tornado_http   | 86.7 ms                                                | 68.1 ms: 1.27x faster                                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 194 ms: 2.00x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 239 ms: 1.98x faster                                                  |
| async_tree_io           | 980 ms                                                 | 544 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 453 ms: 1.43x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.79x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 62.7 ms: 1.48x faster                                                 |
| float          | 69.0 ms                                                | 46.7 ms: 1.48x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 71.2 ms: 1.34x faster                                                 |
| regex_dna      | 174 ms                                                 | 153 ms: 1.14x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.2 ms: 1.00x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 174 us: 1.62x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 131 us: 1.48x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.25 sec: 1.37x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 35.8 ms: 1.30x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.35 ms: 1.28x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 51.7 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 72.8 ms: 1.01x slower                                                 |
| xml_etree_parse      | 108 ms                                                 | 109 ms: 1.02x slower                                                  |
| json_loads           | 16.4 us                                                | 17.3 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.1 ms: 1.48x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.1 ms: 1.65x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.56x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.46 ms: 1.53x faster                                                 |
| django_template | 26.4 ms                                                | 21.6 ms: 1.22x faster                                                 |
| genshi_text     | 17.3 ms                                                | 14.7 ms: 1.18x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 34.9 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.21x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 97.8 us: 3.30x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.32 ms: 2.11x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 17.2 us: 2.02x faster                                                 |
| async_tree_none          | 388 ms                                                 | 194 ms: 2.00x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 239 ms: 1.98x faster                                                  |
| logging_silent           | 117 ns                                                 | 61.0 ns: 1.92x faster                                                 |
| raytrace                 | 301 ms                                                 | 160 ms: 1.88x faster                                                  |
| async_tree_io            | 980 ms                                                 | 544 ms: 1.80x faster                                                  |
| deepcopy                 | 272 us                                                 | 154 us: 1.76x faster                                                  |
| chaos                    | 65.8 ms                                                | 38.8 ms: 1.70x faster                                                 |
| richards_super           | 57.8 ms                                                | 34.2 ms: 1.69x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 174 us: 1.62x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 413 ms: 1.60x faster                                                  |
| richards                 | 48.7 ms                                                | 30.9 ms: 1.58x faster                                                 |
| scimark_lu               | 103 ms                                                 | 66.2 ms: 1.55x faster                                                 |
| mako                     | 9.87 ms                                                | 6.46 ms: 1.53x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.54 us: 1.51x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 43.8 ms: 1.50x faster                                                 |
| logging_simple           | 4.45 us                                                | 2.99 us: 1.49x faster                                                 |
| go                       | 151 ms                                                 | 101 ms: 1.49x faster                                                  |
| nbody                    | 93.0 ms                                                | 62.7 ms: 1.48x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 131 us: 1.48x faster                                                  |
| float                    | 69.0 ms                                                | 46.7 ms: 1.48x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 847 us: 1.47x faster                                                  |
| logging_format           | 4.83 us                                                | 3.30 us: 1.46x faster                                                 |
| scimark_sor              | 128 ms                                                 | 88.4 ms: 1.45x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 453 ms: 1.43x faster                                                  |
| pylint                   | 277 ms                                                 | 194 ms: 1.43x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.02 ms: 1.42x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.43 ms: 1.40x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 51.6 ms: 1.39x faster                                                 |
| comprehensions           | 16.9 us                                                | 12.2 us: 1.39x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 68.3 ms: 1.39x faster                                                 |
| html5lib                 | 42.4 ms                                                | 30.9 ms: 1.37x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.25 sec: 1.37x faster                                                |
| pyflate                  | 427 ms                                                 | 313 ms: 1.36x faster                                                  |
| regex_compile            | 95.3 ms                                                | 71.2 ms: 1.34x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 982 ms: 1.33x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 483 ms: 1.33x faster                                                  |
| thrift                   | 572 us                                                 | 433 us: 1.32x faster                                                  |
| generators               | 32.3 ms                                                | 24.6 ms: 1.31x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 35.8 ms: 1.30x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.28x faster                                                 |
| pycparser                | 877 ms                                                 | 684 ms: 1.28x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.35 ms: 1.28x faster                                                 |
| tornado_http             | 86.7 ms                                                | 68.1 ms: 1.27x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 28.2 ms: 1.25x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 74.2 ms: 1.24x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                                |
| django_template          | 26.4 ms                                                | 21.6 ms: 1.22x faster                                                 |
| fannkuch                 | 303 ms                                                 | 249 ms: 1.22x faster                                                  |
| scimark_fft              | 224 ms                                                 | 189 ms: 1.19x faster                                                  |
| genshi_text              | 17.3 ms                                                | 14.7 ms: 1.18x faster                                                 |
| sympy_str                | 165 ms                                                 | 142 ms: 1.17x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 11.3 ms: 1.17x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.01 ms: 1.14x faster                                                 |
| regex_dna                | 174 ms                                                 | 153 ms: 1.14x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.54 sec: 1.13x faster                                                |
| bench_thread_pool        | 527 us                                                 | 472 us: 1.12x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.46 sec: 1.11x faster                                                |
| nqueens                  | 63.8 ms                                                | 57.8 ms: 1.10x faster                                                 |
| 2to3                     | 192 ms                                                 | 174 ms: 1.10x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 33.4 ms: 1.10x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 71.0 ms: 1.09x faster                                                 |
| sympy_expand             | 269 ms                                                 | 246 ms: 1.09x faster                                                  |
| dask                     | 253 ms                                                 | 233 ms: 1.08x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 179 ms: 1.06x faster                                                  |
| json                     | 3.08 ms                                                | 2.91 ms: 1.06x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.5 ms: 1.04x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 51.7 ms: 1.03x faster                                                 |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.2 ms: 1.00x slower                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 72.8 ms: 1.01x slower                                                 |
| xml_etree_parse          | 108 ms                                                 | 109 ms: 1.02x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 34.9 ms: 1.03x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.47 ms: 1.04x slower                                                 |
| json_loads               | 16.4 us                                                | 17.3 us: 1.05x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 904 us: 1.05x slower                                                  |
| coverage                 | 41.5 ms                                                | 44.7 ms: 1.08x slower                                                 |
| async_generators         | 231 ms                                                 | 295 ms: 1.28x slower                                                  |
| telco                    | 3.49 ms                                                | 4.56 ms: 1.31x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 51.0 ms: 1.36x slower                                                 |
| python_startup           | 10.9 ms                                                | 16.1 ms: 1.48x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.1 ms: 1.65x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 0.93x