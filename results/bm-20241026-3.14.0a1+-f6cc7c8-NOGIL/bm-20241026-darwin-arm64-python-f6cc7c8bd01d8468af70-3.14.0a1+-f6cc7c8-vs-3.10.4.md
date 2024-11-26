# Results vs. 3.10.4

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: darwin-arm64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.109x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.45x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 242 ms: 1.26x slower                                                   |
| docutils       | 1.73 sec                                               | 1.68 sec: 1.03x faster                                                 |
| html5lib       | 42.4 ms                                                | 50.3 ms: 1.19x slower                                                  |
| tornado_http   | 86.7 ms                                                | 108 ms: 1.25x slower                                                   |
| Geometric mean | (ref)                                                  | 1.16x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 515 ms: 1.90x faster                                                   |
| async_tree_none         | 388 ms                                                 | 227 ms: 1.71x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 283 ms: 1.67x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 483 ms: 1.34x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.64x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                   |
| float          | 69.0 ms                                                | 93.1 ms: 1.35x slower                                                  |
| nbody          | 93.0 ms                                                | 149 ms: 1.61x slower                                                   |
| Geometric mean | (ref)                                                  | 1.29x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 135 ms: 1.29x faster                                                   |
| regex_v8       | 17.1 ms                                                | 16.3 ms: 1.05x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.35 ms: 1.05x faster                                                  |
| regex_compile  | 95.3 ms                                                | 118 ms: 1.24x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 98.2 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 74.9 ms: 1.04x slower                                                  |
| json_dumps           | 8.11 ms                                                | 8.69 ms: 1.07x slower                                                  |
| json_loads           | 16.4 us                                                | 18.2 us: 1.11x slower                                                  |
| xml_etree_process    | 46.5 ms                                                | 53.2 ms: 1.14x slower                                                  |
| tomli_loads          | 1.71 sec                                               | 1.97 sec: 1.16x slower                                                 |
| pickle_pure_python   | 281 us                                                 | 338 us: 1.20x slower                                                   |
| xml_etree_generate   | 53.5 ms                                                | 65.6 ms: 1.23x slower                                                  |
| unpickle_pure_python | 194 us                                                 | 261 us: 1.34x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 20.6 ms: 1.90x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 16.1 ms: 2.03x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.96x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 26.4 ms                                                | 34.1 ms: 1.29x slower                                                  |
| genshi_text     | 17.3 ms                                                | 23.5 ms: 1.35x slower                                                  |
| mako            | 9.87 ms                                                | 13.4 ms: 1.36x slower                                                  |
| genshi_xml      | 33.8 ms                                                | 48.0 ms: 1.42x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.36x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 143 us: 2.26x faster                                                   |
| async_tree_io            | 980 ms                                                 | 515 ms: 1.90x faster                                                   |
| asyncio_websockets       | 410 ms                                                 | 238 ms: 1.72x faster                                                   |
| async_tree_none          | 388 ms                                                 | 227 ms: 1.71x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 283 ms: 1.67x faster                                                   |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 483 ms: 1.34x faster                                                   |
| pylint                   | 277 ms                                                 | 209 ms: 1.32x faster                                                   |
| regex_dna                | 174 ms                                                 | 135 ms: 1.29x faster                                                   |
| deepcopy_memo            | 34.7 us                                                | 29.9 us: 1.16x faster                                                  |
| deepcopy                 | 272 us                                                 | 234 us: 1.16x faster                                                   |
| xml_etree_parse          | 108 ms                                                 | 98.2 ms: 1.10x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 16.3 ms: 1.05x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.35 ms: 1.05x faster                                                  |
| generators               | 32.3 ms                                                | 31.0 ms: 1.04x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.68 sec: 1.03x faster                                                 |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                   |
| deepcopy_reduce          | 2.33 us                                                | 2.34 us: 1.00x slower                                                  |
| pycparser                | 877 ms                                                 | 909 ms: 1.04x slower                                                   |
| xml_etree_iterparse      | 72.1 ms                                                | 74.9 ms: 1.04x slower                                                  |
| json                     | 3.08 ms                                                | 3.22 ms: 1.04x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.51 ms: 1.06x slower                                                  |
| richards_super           | 57.8 ms                                                | 61.9 ms: 1.07x slower                                                  |
| json_dumps               | 8.11 ms                                                | 8.69 ms: 1.07x slower                                                  |
| crypto_pyaes             | 71.8 ms                                                | 78.4 ms: 1.09x slower                                                  |
| deltablue                | 4.91 ms                                                | 5.41 ms: 1.10x slower                                                  |
| coroutines               | 20.7 ms                                                | 22.8 ms: 1.10x slower                                                  |
| richards                 | 48.7 ms                                                | 53.7 ms: 1.10x slower                                                  |
| json_loads               | 16.4 us                                                | 18.2 us: 1.11x slower                                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 9.86 ms: 1.11x slower                                                  |
| pyflate                  | 427 ms                                                 | 477 ms: 1.12x slower                                                   |
| mdp                      | 1.63 sec                                               | 1.82 sec: 1.12x slower                                                 |
| logging_silent           | 117 ns                                                 | 131 ns: 1.12x slower                                                   |
| comprehensions           | 16.9 us                                                | 19.1 us: 1.13x slower                                                  |
| meteor_contest           | 77.7 ms                                                | 88.1 ms: 1.13x slower                                                  |
| dulwich_log              | 35.3 ms                                                | 40.2 ms: 1.14x slower                                                  |
| thrift                   | 572 us                                                 | 650 us: 1.14x slower                                                   |
| chaos                    | 65.8 ms                                                | 75.1 ms: 1.14x slower                                                  |
| xml_etree_process        | 46.5 ms                                                | 53.2 ms: 1.14x slower                                                  |
| nqueens                  | 63.8 ms                                                | 73.4 ms: 1.15x slower                                                  |
| tomli_loads              | 1.71 sec                                               | 1.97 sec: 1.16x slower                                                 |
| scimark_fft              | 224 ms                                                 | 262 ms: 1.17x slower                                                   |
| fannkuch                 | 303 ms                                                 | 356 ms: 1.18x slower                                                   |
| go                       | 151 ms                                                 | 178 ms: 1.18x slower                                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 77.7 ms: 1.18x slower                                                  |
| raytrace                 | 301 ms                                                 | 357 ms: 1.19x slower                                                   |
| html5lib                 | 42.4 ms                                                | 50.3 ms: 1.19x slower                                                  |
| pickle_pure_python       | 281 us                                                 | 338 us: 1.20x slower                                                   |
| sympy_integrate          | 13.1 ms                                                | 15.9 ms: 1.21x slower                                                  |
| scimark_sor              | 128 ms                                                 | 156 ms: 1.22x slower                                                   |
| sqlalchemy_declarative   | 73.3 ms                                                | 89.3 ms: 1.22x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 65.6 ms: 1.23x slower                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 4.22 ms: 1.23x slower                                                  |
| hexiom                   | 6.19 ms                                                | 7.66 ms: 1.24x slower                                                  |
| regex_compile            | 95.3 ms                                                | 118 ms: 1.24x slower                                                   |
| pprint_pformat           | 1.30 sec                                               | 1.62 sec: 1.24x slower                                                 |
| pprint_safe_repr         | 641 ms                                                 | 796 ms: 1.24x slower                                                   |
| tornado_http             | 86.7 ms                                                | 108 ms: 1.25x slower                                                   |
| 2to3                     | 192 ms                                                 | 242 ms: 1.26x slower                                                   |
| create_gc_cycles         | 860 us                                                 | 1.09 ms: 1.27x slower                                                  |
| coverage                 | 41.5 ms                                                | 52.9 ms: 1.28x slower                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.84 ms: 1.28x slower                                                  |
| logging_simple           | 4.45 us                                                | 5.70 us: 1.28x slower                                                  |
| logging_format           | 4.83 us                                                | 6.22 us: 1.29x slower                                                  |
| django_template          | 26.4 ms                                                | 34.1 ms: 1.29x slower                                                  |
| sqlglot_parse            | 1.24 ms                                                | 1.63 ms: 1.31x slower                                                  |
| spectral_norm            | 94.8 ms                                                | 127 ms: 1.34x slower                                                   |
| unpickle_pure_python     | 194 us                                                 | 261 us: 1.34x slower                                                   |
| float                    | 69.0 ms                                                | 93.1 ms: 1.35x slower                                                  |
| genshi_text              | 17.3 ms                                                | 23.5 ms: 1.35x slower                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 49.9 ms: 1.36x slower                                                  |
| mako                     | 9.87 ms                                                | 13.4 ms: 1.36x slower                                                  |
| sympy_str                | 165 ms                                                 | 226 ms: 1.37x slower                                                   |
| sqlglot_normalize        | 190 ms                                                 | 261 ms: 1.37x slower                                                   |
| scimark_lu               | 103 ms                                                 | 142 ms: 1.38x slower                                                   |
| async_generators         | 231 ms                                                 | 327 ms: 1.41x slower                                                   |
| genshi_xml               | 33.8 ms                                                | 48.0 ms: 1.42x slower                                                  |
| sympy_sum                | 92.2 ms                                                | 136 ms: 1.48x slower                                                   |
| bench_thread_pool        | 527 us                                                 | 794 us: 1.51x slower                                                   |
| sympy_expand             | 269 ms                                                 | 415 ms: 1.54x slower                                                   |
| telco                    | 3.49 ms                                                | 5.43 ms: 1.56x slower                                                  |
| nbody                    | 93.0 ms                                                | 149 ms: 1.61x slower                                                   |
| bench_mp_pool            | 37.4 ms                                                | 68.9 ms: 1.84x slower                                                  |
| python_startup           | 10.9 ms                                                | 20.6 ms: 1.90x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 16.1 ms: 2.03x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.13x slower                                                           |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241026-3.14.0a1+-f6cc7c8-NOGIL/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.109x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.45x