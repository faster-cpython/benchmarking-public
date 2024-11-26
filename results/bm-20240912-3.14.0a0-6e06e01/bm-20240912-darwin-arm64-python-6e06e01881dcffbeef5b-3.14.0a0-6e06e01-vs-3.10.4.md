# Results vs. 3.10.4

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: darwin-arm64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.302x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 0.68x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 160 ms: 1.19x faster                                                  |
| docutils       | 1.73 sec                                               | 1.43 sec: 1.21x faster                                                |
| html5lib       | 42.4 ms                                                | 30.2 ms: 1.40x faster                                                 |
| Geometric mean | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 199 ms: 1.96x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 246 ms: 1.93x faster                                                  |
| async_tree_io           | 980 ms                                                 | 579 ms: 1.69x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 465 ms: 1.40x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.9 ms: 1.53x faster                                                 |
| float          | 69.0 ms                                                | 49.3 ms: 1.40x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 66.9 ms: 1.42x faster                                                 |
| regex_dna      | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 182 us: 1.54x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 141 us: 1.38x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.39 ms: 1.27x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.3 ms: 1.25x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.48 sec: 1.15x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 53.2 ms: 1.01x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 74.2 ms: 1.03x slower                                                 |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                                 |
| unpickle             | 8.80 us                                                | 9.21 us: 1.05x slower                                                 |
| pickle               | 6.97 us                                                | 7.48 us: 1.07x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.95 us: 1.08x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.94 us: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.1 ms: 1.39x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 12.4 ms: 1.57x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.48x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.89 ms: 1.43x faster                                                 |
| django_template | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                 |
| genshi_text     | 17.3 ms                                                | 14.0 ms: 1.24x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.3 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 91.5 us: 3.53x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.14 ms: 2.30x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.5 us: 2.10x faster                                                 |
| raytrace                 | 301 ms                                                 | 150 ms: 2.01x faster                                                  |
| async_tree_none          | 388 ms                                                 | 199 ms: 1.96x faster                                                  |
| logging_silent           | 117 ns                                                 | 60.8 ns: 1.93x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 246 ms: 1.93x faster                                                  |
| go                       | 151 ms                                                 | 79.0 ms: 1.91x faster                                                 |
| deepcopy                 | 272 us                                                 | 144 us: 1.88x faster                                                  |
| chaos                    | 65.8 ms                                                | 35.8 ms: 1.84x faster                                                 |
| comprehensions           | 16.9 us                                                | 9.99 us: 1.69x faster                                                 |
| async_tree_io            | 980 ms                                                 | 579 ms: 1.69x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 744 us: 1.67x faster                                                  |
| richards_super           | 57.8 ms                                                | 35.4 ms: 1.64x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 905 us: 1.59x faster                                                  |
| generators               | 32.3 ms                                                | 20.4 ms: 1.58x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 422 ms: 1.56x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.55x faster                                                 |
| richards                 | 48.7 ms                                                | 31.5 ms: 1.55x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 182 us: 1.54x faster                                                  |
| nbody                    | 93.0 ms                                                | 60.9 ms: 1.53x faster                                                 |
| pylint                   | 277 ms                                                 | 181 ms: 1.53x faster                                                  |
| scimark_lu               | 103 ms                                                 | 67.6 ms: 1.52x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 43.2 ms: 1.52x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.10 ms: 1.51x faster                                                 |
| unpack_sequence          | 39.0 ns                                                | 26.7 ns: 1.46x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.06 us: 1.45x faster                                                 |
| logging_format           | 4.83 us                                                | 3.36 us: 1.44x faster                                                 |
| mako                     | 9.87 ms                                                | 6.89 ms: 1.43x faster                                                 |
| regex_compile            | 95.3 ms                                                | 66.9 ms: 1.42x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 50.5 ms: 1.42x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 452 ms: 1.42x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 924 ms: 1.41x faster                                                  |
| html5lib                 | 42.4 ms                                                | 30.2 ms: 1.40x faster                                                 |
| float                    | 69.0 ms                                                | 49.3 ms: 1.40x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 465 ms: 1.40x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 68.0 ms: 1.39x faster                                                 |
| scimark_sor              | 128 ms                                                 | 93.0 ms: 1.38x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 141 us: 1.38x faster                                                  |
| pycparser                | 877 ms                                                 | 639 ms: 1.37x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 68.5 ms: 1.35x faster                                                 |
| thrift                   | 572 us                                                 | 426 us: 1.34x faster                                                  |
| django_template          | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                 |
| pyflate                  | 427 ms                                                 | 322 ms: 1.33x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 27.2 ms: 1.30x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.28x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.39 ms: 1.27x faster                                                 |
| sympy_str                | 165 ms                                                 | 131 ms: 1.26x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.25x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 37.3 ms: 1.25x faster                                                 |
| genshi_text              | 17.3 ms                                                | 14.0 ms: 1.24x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.9 ms: 1.23x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.79 ms: 1.23x faster                                                 |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.21x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.43 sec: 1.21x faster                                                |
| regex_dna                | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| 2to3                     | 192 ms                                                 | 160 ms: 1.19x faster                                                  |
| sympy_expand             | 269 ms                                                 | 226 ms: 1.19x faster                                                  |
| nqueens                  | 63.8 ms                                                | 53.6 ms: 1.19x faster                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 31.3 ms: 1.18x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 450 us: 1.17x faster                                                  |
| fannkuch                 | 303 ms                                                 | 261 ms: 1.16x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.48 sec: 1.15x faster                                                |
| mdp                      | 1.63 sec                                               | 1.42 sec: 1.15x faster                                                |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 30.3 ms: 1.11x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 72.0 ms: 1.08x faster                                                 |
| pathlib                  | 24.5 ms                                                | 22.9 ms: 1.07x faster                                                 |
| json                     | 3.08 ms                                                | 2.95 ms: 1.05x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 53.2 ms: 1.01x faster                                                 |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 74.2 ms: 1.03x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                                 |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 897 us: 1.04x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.21 us: 1.05x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.55 us: 1.06x slower                                                 |
| pickle                   | 6.97 us                                                | 7.48 us: 1.07x slower                                                 |
| coverage                 | 41.5 ms                                                | 44.6 ms: 1.07x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.95 us: 1.08x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.94 us: 1.09x slower                                                 |
| async_generators         | 231 ms                                                 | 280 ms: 1.21x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 48.1 ms: 1.29x slower                                                 |
| telco                    | 3.49 ms                                                | 4.82 ms: 1.38x slower                                                 |
| python_startup           | 10.9 ms                                                | 15.1 ms: 1.39x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 12.4 ms: 1.57x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                          |

Benchmark hidden because not significant (3): tornado_http, asyncio_websockets, regex_effbot
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.302x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 0.68x