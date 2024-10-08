# Results vs. 3.10.4

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: darwin-arm64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.14x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 0.68x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 249 ms: 1.30x slower                                                  |
| docutils       | 1.73 sec                                               | 1.78 sec: 1.03x slower                                                |
| html5lib       | 42.4 ms                                                | 51.8 ms: 1.22x slower                                                 |
| tornado_http   | 86.7 ms                                                | 103 ms: 1.18x slower                                                  |
| Geometric mean | (ref)                                                  | 1.18x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 541 ms: 1.81x faster                                                  |
| async_tree_none         | 388 ms                                                 | 239 ms: 1.62x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 296 ms: 1.60x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 494 ms: 1.32x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.58x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                                  |
| float          | 69.0 ms                                                | 97.7 ms: 1.42x slower                                                 |
| nbody          | 93.0 ms                                                | 157 ms: 1.69x slower                                                  |
| Geometric mean | (ref)                                                  | 1.34x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 139 ms: 1.26x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                 |
| regex_v8       | 17.1 ms                                                | 17.2 ms: 1.01x slower                                                 |
| regex_compile  | 95.3 ms                                                | 121 ms: 1.28x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| json_dumps           | 8.11 ms                                                | 7.92 ms: 1.02x faster                                                 |
| pickle               | 6.97 us                                                | 7.01 us: 1.00x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.89 us: 1.05x slower                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 77.1 ms: 1.07x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.4 us: 1.08x slower                                                 |
| unpickle             | 8.80 us                                                | 9.84 us: 1.12x slower                                                 |
| json_loads           | 16.4 us                                                | 19.2 us: 1.17x slower                                                 |
| tomli_loads          | 1.71 sec                                               | 2.03 sec: 1.19x slower                                                |
| unpickle_list        | 2.69 us                                                | 3.22 us: 1.20x slower                                                 |
| pickle_pure_python   | 281 us                                                 | 348 us: 1.24x slower                                                  |
| xml_etree_process    | 46.5 ms                                                | 58.3 ms: 1.25x slower                                                 |
| xml_etree_generate   | 53.5 ms                                                | 70.1 ms: 1.31x slower                                                 |
| unpickle_pure_python | 194 us                                                 | 265 us: 1.36x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.14x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 19.2 ms: 1.76x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 15.6 ms: 1.97x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.86x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 26.4 ms                                                | 35.9 ms: 1.36x slower                                                 |
| mako            | 9.87 ms                                                | 13.5 ms: 1.36x slower                                                 |
| genshi_text     | 17.3 ms                                                | 25.3 ms: 1.46x slower                                                 |
| genshi_xml      | 33.8 ms                                                | 50.2 ms: 1.48x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.42x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 144 us: 2.24x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 353 ms: 1.87x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 105 ms: 1.82x faster                                                  |
| async_tree_io            | 980 ms                                                 | 541 ms: 1.81x faster                                                  |
| async_tree_none          | 388 ms                                                 | 239 ms: 1.62x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 296 ms: 1.60x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 494 ms: 1.32x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.24 sec: 1.29x faster                                                |
| regex_dna                | 174 ms                                                 | 139 ms: 1.26x faster                                                  |
| pylint                   | 277 ms                                                 | 220 ms: 1.26x faster                                                  |
| create_gc_cycles         | 860 us                                                 | 699 us: 1.23x faster                                                  |
| gc_traversal             | 2.36 ms                                                | 2.06 ms: 1.15x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 31.6 us: 1.10x faster                                                 |
| deepcopy                 | 272 us                                                 | 249 us: 1.09x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| json_dumps               | 8.11 ms                                                | 7.92 ms: 1.02x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 405 ms: 1.01x faster                                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.01x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                 |
| pickle                   | 6.97 us                                                | 7.01 us: 1.00x slower                                                 |
| regex_v8                 | 17.1 ms                                                | 17.2 ms: 1.01x slower                                                 |
| docutils                 | 1.73 sec                                               | 1.78 sec: 1.03x slower                                                |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.05x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.89 us: 1.05x slower                                                 |
| pycparser                | 877 ms                                                 | 935 ms: 1.07x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 77.1 ms: 1.07x slower                                                 |
| deepcopy_reduce          | 2.33 us                                                | 2.49 us: 1.07x slower                                                 |
| generators               | 32.3 ms                                                | 35.0 ms: 1.08x slower                                                 |
| crypto_pyaes             | 71.8 ms                                                | 77.8 ms: 1.08x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.4 us: 1.08x slower                                                 |
| pathlib                  | 24.5 ms                                                | 26.7 ms: 1.09x slower                                                 |
| json                     | 3.08 ms                                                | 3.41 ms: 1.11x slower                                                 |
| comprehensions           | 16.9 us                                                | 18.9 us: 1.12x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.84 us: 1.12x slower                                                 |
| mdp                      | 1.63 sec                                               | 1.84 sec: 1.13x slower                                                |
| pyflate                  | 427 ms                                                 | 484 ms: 1.14x slower                                                  |
| richards_super           | 57.8 ms                                                | 65.7 ms: 1.14x slower                                                 |
| meteor_contest           | 77.7 ms                                                | 89.5 ms: 1.15x slower                                                 |
| chaos                    | 65.8 ms                                                | 76.0 ms: 1.16x slower                                                 |
| dulwich_log              | 35.3 ms                                                | 41.2 ms: 1.17x slower                                                 |
| deltablue                | 4.91 ms                                                | 5.74 ms: 1.17x slower                                                 |
| richards                 | 48.7 ms                                                | 57.0 ms: 1.17x slower                                                 |
| json_loads               | 16.4 us                                                | 19.2 us: 1.17x slower                                                 |
| logging_silent           | 117 ns                                                 | 137 ns: 1.17x slower                                                  |
| fannkuch                 | 303 ms                                                 | 358 ms: 1.18x slower                                                  |
| tornado_http             | 86.7 ms                                                | 103 ms: 1.18x slower                                                  |
| tomli_loads              | 1.71 sec                                               | 2.03 sec: 1.19x slower                                                |
| nqueens                  | 63.8 ms                                                | 76.1 ms: 1.19x slower                                                 |
| sympy_integrate          | 13.1 ms                                                | 15.7 ms: 1.19x slower                                                 |
| unpickle_list            | 2.69 us                                                | 3.22 us: 1.20x slower                                                 |
| thrift                   | 572 us                                                 | 692 us: 1.21x slower                                                  |
| coroutines               | 20.7 ms                                                | 25.1 ms: 1.21x slower                                                 |
| scimark_fft              | 224 ms                                                 | 274 ms: 1.22x slower                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 4.19 ms: 1.22x slower                                                 |
| go                       | 151 ms                                                 | 184 ms: 1.22x slower                                                  |
| html5lib                 | 42.4 ms                                                | 51.8 ms: 1.22x slower                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 81.1 ms: 1.24x slower                                                 |
| pickle_pure_python       | 281 us                                                 | 348 us: 1.24x slower                                                  |
| xml_etree_process        | 46.5 ms                                                | 58.3 ms: 1.25x slower                                                 |
| hexiom                   | 6.19 ms                                                | 7.77 ms: 1.25x slower                                                 |
| spectral_norm            | 94.8 ms                                                | 120 ms: 1.26x slower                                                  |
| raytrace                 | 301 ms                                                 | 381 ms: 1.26x slower                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.66 sec: 1.27x slower                                                |
| pprint_safe_repr         | 641 ms                                                 | 817 ms: 1.28x slower                                                  |
| regex_compile            | 95.3 ms                                                | 121 ms: 1.28x slower                                                  |
| 2to3                     | 192 ms                                                 | 249 ms: 1.30x slower                                                  |
| scimark_sor              | 128 ms                                                 | 167 ms: 1.31x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 70.1 ms: 1.31x slower                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.94 ms: 1.34x slower                                                 |
| django_template          | 26.4 ms                                                | 35.9 ms: 1.36x slower                                                 |
| sqlglot_parse            | 1.24 ms                                                | 1.69 ms: 1.36x slower                                                 |
| mako                     | 9.87 ms                                                | 13.5 ms: 1.36x slower                                                 |
| unpickle_pure_python     | 194 us                                                 | 265 us: 1.36x slower                                                  |
| coverage                 | 41.5 ms                                                | 56.9 ms: 1.37x slower                                                 |
| logging_simple           | 4.45 us                                                | 6.17 us: 1.39x slower                                                 |
| logging_format           | 4.83 us                                                | 6.73 us: 1.39x slower                                                 |
| sympy_str                | 165 ms                                                 | 234 ms: 1.42x slower                                                  |
| float                    | 69.0 ms                                                | 97.7 ms: 1.42x slower                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 52.4 ms: 1.43x slower                                                 |
| async_generators         | 231 ms                                                 | 332 ms: 1.43x slower                                                  |
| genshi_text              | 17.3 ms                                                | 25.3 ms: 1.46x slower                                                 |
| scimark_lu               | 103 ms                                                 | 152 ms: 1.48x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 50.2 ms: 1.48x slower                                                 |
| bench_thread_pool        | 527 us                                                 | 798 us: 1.51x slower                                                  |
| sympy_sum                | 92.2 ms                                                | 140 ms: 1.52x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 56.8 ms: 1.52x slower                                                 |
| sympy_expand             | 269 ms                                                 | 432 ms: 1.61x slower                                                  |
| telco                    | 3.49 ms                                                | 5.90 ms: 1.69x slower                                                 |
| nbody                    | 93.0 ms                                                | 157 ms: 1.69x slower                                                  |
| python_startup           | 10.9 ms                                                | 19.2 ms: 1.76x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 15.6 ms: 1.97x slower                                                 |
| unpack_sequence          | 39.0 ns                                                | 97.9 ns: 2.51x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.14x slower                                                          |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240914-3.14.0a0-401fff7-NOGIL/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 0.68x