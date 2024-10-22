# Results vs. 3.10.4

- fork: python
- ref: a2bec77d25b11f50362a
- machine: darwin-arm64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.14x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 250 ms: 1.31x slower                                                  |
| docutils       | 1.73 sec                                               | 1.80 sec: 1.04x slower                                                |
| html5lib       | 42.4 ms                                                | 52.4 ms: 1.24x slower                                                 |
| tornado_http   | 86.7 ms                                                | 96.0 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.17x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 538 ms: 1.82x faster                                                  |
| async_tree_none         | 388 ms                                                 | 235 ms: 1.65x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 292 ms: 1.62x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 491 ms: 1.32x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.59x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| float          | 69.0 ms                                                | 96.6 ms: 1.40x slower                                                 |
| nbody          | 93.0 ms                                                | 159 ms: 1.71x slower                                                  |
| Geometric mean | (ref)                                                  | 1.34x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 139 ms: 1.25x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.43 ms: 1.01x faster                                                 |
| regex_v8       | 17.1 ms                                                | 17.5 ms: 1.02x slower                                                 |
| regex_compile  | 95.3 ms                                                | 125 ms: 1.31x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 98.9 ms: 1.09x faster                                                 |
| json_dumps           | 8.11 ms                                                | 8.14 ms: 1.00x slower                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 76.8 ms: 1.06x slower                                                 |
| json_loads           | 16.4 us                                                | 19.3 us: 1.18x slower                                                 |
| tomli_loads          | 1.71 sec                                               | 2.06 sec: 1.21x slower                                                |
| pickle_pure_python   | 281 us                                                 | 346 us: 1.23x slower                                                  |
| xml_etree_process    | 46.5 ms                                                | 60.9 ms: 1.31x slower                                                 |
| xml_etree_generate   | 53.5 ms                                                | 70.7 ms: 1.32x slower                                                 |
| unpickle_pure_python | 194 us                                                 | 269 us: 1.38x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.3 ms: 1.59x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 14.0 ms: 1.77x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.68x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 13.4 ms: 1.36x slower                                                 |
| django_template | 26.4 ms                                                | 35.9 ms: 1.36x slower                                                 |
| genshi_text     | 17.3 ms                                                | 25.8 ms: 1.48x slower                                                 |
| genshi_xml      | 33.8 ms                                                | 51.6 ms: 1.53x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.43x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 149 us: 2.17x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 353 ms: 1.87x faster                                                  |
| async_tree_io            | 980 ms                                                 | 538 ms: 1.82x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 109 ms: 1.74x faster                                                  |
| async_tree_none          | 388 ms                                                 | 235 ms: 1.65x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 292 ms: 1.62x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 491 ms: 1.32x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.24 sec: 1.30x faster                                                |
| create_gc_cycles         | 860 us                                                 | 665 us: 1.29x faster                                                  |
| pylint                   | 277 ms                                                 | 218 ms: 1.27x faster                                                  |
| regex_dna                | 174 ms                                                 | 139 ms: 1.25x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 30.9 us: 1.12x faster                                                 |
| gc_traversal             | 2.36 ms                                                | 2.11 ms: 1.12x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 98.9 ms: 1.09x faster                                                 |
| deepcopy                 | 272 us                                                 | 252 us: 1.08x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.43 ms: 1.01x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 406 ms: 1.01x faster                                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| json_dumps               | 8.11 ms                                                | 8.14 ms: 1.00x slower                                                 |
| regex_v8                 | 17.1 ms                                                | 17.5 ms: 1.02x slower                                                 |
| docutils                 | 1.73 sec                                               | 1.80 sec: 1.04x slower                                                |
| pathlib                  | 24.5 ms                                                | 25.9 ms: 1.06x slower                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 76.8 ms: 1.06x slower                                                 |
| pycparser                | 877 ms                                                 | 955 ms: 1.09x slower                                                  |
| deepcopy_reduce          | 2.33 us                                                | 2.55 us: 1.09x slower                                                 |
| crypto_pyaes             | 71.8 ms                                                | 79.5 ms: 1.11x slower                                                 |
| tornado_http             | 86.7 ms                                                | 96.0 ms: 1.11x slower                                                 |
| json                     | 3.08 ms                                                | 3.42 ms: 1.11x slower                                                 |
| coroutines               | 20.7 ms                                                | 23.1 ms: 1.12x slower                                                 |
| pyflate                  | 427 ms                                                 | 482 ms: 1.13x slower                                                  |
| comprehensions           | 16.9 us                                                | 19.3 us: 1.14x slower                                                 |
| generators               | 32.3 ms                                                | 37.0 ms: 1.14x slower                                                 |
| richards_super           | 57.8 ms                                                | 66.5 ms: 1.15x slower                                                 |
| logging_silent           | 117 ns                                                 | 135 ns: 1.15x slower                                                  |
| mdp                      | 1.63 sec                                               | 1.88 sec: 1.16x slower                                                |
| chaos                    | 65.8 ms                                                | 76.5 ms: 1.16x slower                                                 |
| richards                 | 48.7 ms                                                | 56.8 ms: 1.17x slower                                                 |
| deltablue                | 4.91 ms                                                | 5.76 ms: 1.17x slower                                                 |
| json_loads               | 16.4 us                                                | 19.3 us: 1.18x slower                                                 |
| meteor_contest           | 77.7 ms                                                | 91.5 ms: 1.18x slower                                                 |
| fannkuch                 | 303 ms                                                 | 359 ms: 1.19x slower                                                  |
| sympy_integrate          | 13.1 ms                                                | 15.8 ms: 1.20x slower                                                 |
| tomli_loads              | 1.71 sec                                               | 2.06 sec: 1.21x slower                                                |
| scimark_monte_carlo      | 65.6 ms                                                | 80.5 ms: 1.23x slower                                                 |
| pickle_pure_python       | 281 us                                                 | 346 us: 1.23x slower                                                  |
| scimark_fft              | 224 ms                                                 | 277 ms: 1.23x slower                                                  |
| thrift                   | 572 us                                                 | 706 us: 1.23x slower                                                  |
| raytrace                 | 301 ms                                                 | 373 ms: 1.24x slower                                                  |
| html5lib                 | 42.4 ms                                                | 52.4 ms: 1.24x slower                                                 |
| nqueens                  | 63.8 ms                                                | 79.2 ms: 1.24x slower                                                 |
| scimark_sor              | 128 ms                                                 | 160 ms: 1.25x slower                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 4.35 ms: 1.27x slower                                                 |
| spectral_norm            | 94.8 ms                                                | 122 ms: 1.28x slower                                                  |
| hexiom                   | 6.19 ms                                                | 8.02 ms: 1.30x slower                                                 |
| 2to3                     | 192 ms                                                 | 250 ms: 1.31x slower                                                  |
| regex_compile            | 95.3 ms                                                | 125 ms: 1.31x slower                                                  |
| xml_etree_process        | 46.5 ms                                                | 60.9 ms: 1.31x slower                                                 |
| xml_etree_generate       | 53.5 ms                                                | 70.7 ms: 1.32x slower                                                 |
| go                       | 151 ms                                                 | 200 ms: 1.33x slower                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.73 sec: 1.33x slower                                                |
| pprint_safe_repr         | 641 ms                                                 | 851 ms: 1.33x slower                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.95 ms: 1.35x slower                                                 |
| mako                     | 9.87 ms                                                | 13.4 ms: 1.36x slower                                                 |
| django_template          | 26.4 ms                                                | 35.9 ms: 1.36x slower                                                 |
| coverage                 | 41.5 ms                                                | 56.5 ms: 1.36x slower                                                 |
| sqlglot_parse            | 1.24 ms                                                | 1.71 ms: 1.37x slower                                                 |
| unpickle_pure_python     | 194 us                                                 | 269 us: 1.38x slower                                                  |
| logging_simple           | 4.45 us                                                | 6.16 us: 1.38x slower                                                 |
| logging_format           | 4.83 us                                                | 6.72 us: 1.39x slower                                                 |
| float                    | 69.0 ms                                                | 96.6 ms: 1.40x slower                                                 |
| sympy_str                | 165 ms                                                 | 238 ms: 1.44x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 54.6 ms: 1.46x slower                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 54.4 ms: 1.48x slower                                                 |
| async_generators         | 231 ms                                                 | 343 ms: 1.48x slower                                                  |
| genshi_text              | 17.3 ms                                                | 25.8 ms: 1.48x slower                                                 |
| bench_thread_pool        | 527 us                                                 | 790 us: 1.50x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 51.6 ms: 1.53x slower                                                 |
| sympy_sum                | 92.2 ms                                                | 141 ms: 1.53x slower                                                  |
| scimark_lu               | 103 ms                                                 | 159 ms: 1.55x slower                                                  |
| telco                    | 3.49 ms                                                | 5.53 ms: 1.59x slower                                                 |
| python_startup           | 10.9 ms                                                | 17.3 ms: 1.59x slower                                                 |
| sympy_expand             | 269 ms                                                 | 444 ms: 1.65x slower                                                  |
| nbody                    | 93.0 ms                                                | 159 ms: 1.71x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 14.0 ms: 1.77x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.14x slower                                                          |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240713-3.14.0a0-a2bec77-NOGIL/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.15x
- 95% likely to have a slowdown of 1.15x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: 1.30x