# Results vs. 3.10.4

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: darwin-arm64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 0.55x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 164 ms: 1.17x faster                                                  |
| docutils       | 1.73 sec                                               | 1.49 sec: 1.16x faster                                                |
| html5lib       | 42.4 ms                                                | 31.5 ms: 1.35x faster                                                 |
| tornado_http   | 86.7 ms                                                | 66.8 ms: 1.30x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 195 ms: 1.99x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 240 ms: 1.97x faster                                                  |
| async_tree_io           | 980 ms                                                 | 547 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 453 ms: 1.43x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.78x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.6 ms: 1.56x faster                                                 |
| float          | 69.0 ms                                                | 48.4 ms: 1.43x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.4 ms: 1.39x faster                                                 |
| regex_dna      | 174 ms                                                 | 150 ms: 1.16x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.02x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.55 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 184 us: 1.53x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 143 us: 1.36x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.54 ms: 1.24x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.9 ms: 1.23x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.48 sec: 1.15x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 53.4 ms: 1.00x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 74.3 ms: 1.03x slower                                                 |
| json_loads           | 16.4 us                                                | 17.2 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.4 ms: 1.42x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 12.8 ms: 1.61x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.51x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.02 ms: 1.41x faster                                                 |
| django_template | 26.4 ms                                                | 19.9 ms: 1.32x faster                                                 |
| genshi_text     | 17.3 ms                                                | 14.1 ms: 1.23x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.3 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.26x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 94.2 us: 3.43x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.12 ms: 2.32x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.9 us: 2.05x faster                                                 |
| raytrace                 | 301 ms                                                 | 148 ms: 2.03x faster                                                  |
| async_tree_none          | 388 ms                                                 | 195 ms: 1.99x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 240 ms: 1.97x faster                                                  |
| logging_silent           | 117 ns                                                 | 60.0 ns: 1.95x faster                                                 |
| deepcopy                 | 272 us                                                 | 145 us: 1.87x faster                                                  |
| chaos                    | 65.8 ms                                                | 36.0 ms: 1.83x faster                                                 |
| async_tree_io            | 980 ms                                                 | 547 ms: 1.79x faster                                                  |
| richards_super           | 57.8 ms                                                | 34.6 ms: 1.67x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 748 us: 1.66x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 405 ms: 1.63x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 911 us: 1.58x faster                                                  |
| generators               | 32.3 ms                                                | 20.6 ms: 1.57x faster                                                 |
| nbody                    | 93.0 ms                                                | 59.6 ms: 1.56x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.50 us: 1.55x faster                                                 |
| comprehensions           | 16.9 us                                                | 10.9 us: 1.55x faster                                                 |
| go                       | 151 ms                                                 | 97.7 ms: 1.54x faster                                                 |
| richards                 | 48.7 ms                                                | 31.6 ms: 1.54x faster                                                 |
| scimark_lu               | 103 ms                                                 | 67.0 ms: 1.54x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 184 us: 1.53x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.06 ms: 1.53x faster                                                 |
| pylint                   | 277 ms                                                 | 182 ms: 1.52x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 43.3 ms: 1.51x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.05 us: 1.46x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 453 ms: 1.43x faster                                                  |
| logging_format           | 4.83 us                                                | 3.38 us: 1.43x faster                                                 |
| float                    | 69.0 ms                                                | 48.4 ms: 1.43x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 50.4 ms: 1.42x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 66.8 ms: 1.42x faster                                                 |
| mako                     | 9.87 ms                                                | 7.02 ms: 1.41x faster                                                 |
| regex_compile            | 95.3 ms                                                | 68.4 ms: 1.39x faster                                                 |
| scimark_sor              | 128 ms                                                 | 93.2 ms: 1.38x faster                                                 |
| pycparser                | 877 ms                                                 | 642 ms: 1.36x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 470 ms: 1.36x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 958 ms: 1.36x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 143 us: 1.36x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.5 ms: 1.35x faster                                                 |
| pyflate                  | 427 ms                                                 | 321 ms: 1.33x faster                                                  |
| thrift                   | 572 us                                                 | 432 us: 1.33x faster                                                  |
| django_template          | 26.4 ms                                                | 19.9 ms: 1.32x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 27.1 ms: 1.30x faster                                                 |
| tornado_http             | 86.7 ms                                                | 66.8 ms: 1.30x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 71.0 ms: 1.30x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.28x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.5 ms: 1.25x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                                |
| json_dumps               | 8.11 ms                                                | 6.54 ms: 1.24x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.77 ms: 1.24x faster                                                 |
| genshi_text              | 17.3 ms                                                | 14.1 ms: 1.23x faster                                                 |
| sympy_str                | 165 ms                                                 | 135 ms: 1.23x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 37.9 ms: 1.23x faster                                                 |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.21x faster                                                  |
| nqueens                  | 63.8 ms                                                | 53.3 ms: 1.20x faster                                                 |
| 2to3                     | 192 ms                                                 | 164 ms: 1.17x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 452 us: 1.17x faster                                                  |
| regex_dna                | 174 ms                                                 | 150 ms: 1.16x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 31.6 ms: 1.16x faster                                                 |
| sympy_expand             | 269 ms                                                 | 232 ms: 1.16x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.49 sec: 1.16x faster                                                |
| tomli_loads              | 1.71 sec                                               | 1.48 sec: 1.15x faster                                                |
| fannkuch                 | 303 ms                                                 | 263 ms: 1.15x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.42 sec: 1.15x faster                                                |
| genshi_xml               | 33.8 ms                                                | 30.3 ms: 1.12x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 171 ms: 1.11x faster                                                  |
| dask                     | 253 ms                                                 | 230 ms: 1.10x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 72.1 ms: 1.08x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.1 ms: 1.06x faster                                                 |
| json                     | 3.08 ms                                                | 2.96 ms: 1.04x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 53.4 ms: 1.00x faster                                                 |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.02x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 878 us: 1.02x slower                                                  |
| xml_etree_parse          | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 74.3 ms: 1.03x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.55 ms: 1.04x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| json_loads               | 16.4 us                                                | 17.2 us: 1.04x slower                                                 |
| coverage                 | 41.5 ms                                                | 44.3 ms: 1.07x slower                                                 |
| async_generators         | 231 ms                                                 | 280 ms: 1.21x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 48.3 ms: 1.29x slower                                                 |
| telco                    | 3.49 ms                                                | 4.60 ms: 1.32x slower                                                 |
| python_startup           | 10.9 ms                                                | 15.4 ms: 1.42x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 12.8 ms: 1.61x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 0.55x