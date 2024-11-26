# Results vs. 3.10.4

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: darwin-arm64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.226x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 0.52x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 178 ms: 1.08x faster                                                  |
| docutils       | 1.73 sec                                               | 1.57 sec: 1.10x faster                                                |
| html5lib       | 42.4 ms                                                | 32.8 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 203 ms: 1.91x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 251 ms: 1.89x faster                                                  |
| async_tree_io           | 980 ms                                                 | 597 ms: 1.64x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 470 ms: 1.38x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.69x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.6 ms: 1.48x faster                                                 |
| nbody          | 93.0 ms                                                | 63.5 ms: 1.47x faster                                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 74.9 ms: 1.27x faster                                                 |
| regex_dna      | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.47 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 179 us: 1.57x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 131 us: 1.48x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.24 sec: 1.37x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 34.6 ms: 1.34x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.36 ms: 1.27x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 51.3 ms: 1.04x faster                                                 |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                                 |
| pickle               | 6.97 us                                                | 7.39 us: 1.06x slower                                                 |
| unpickle             | 8.80 us                                                | 9.37 us: 1.07x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.91 us: 1.08x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.96 us: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.1 ms: 1.57x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 14.1 ms: 1.78x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.67x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.51 ms: 1.52x faster                                                 |
| django_template | 26.4 ms                                                | 23.2 ms: 1.14x faster                                                 |
| genshi_text     | 17.3 ms                                                | 16.8 ms: 1.03x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 41.6 ms: 1.23x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 96.1 us: 3.36x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.2 us: 2.15x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.36 ms: 2.08x faster                                                 |
| async_tree_none          | 388 ms                                                 | 203 ms: 1.91x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 251 ms: 1.89x faster                                                  |
| logging_silent           | 117 ns                                                 | 62.1 ns: 1.89x faster                                                 |
| deepcopy                 | 272 us                                                 | 154 us: 1.76x faster                                                  |
| raytrace                 | 301 ms                                                 | 174 ms: 1.73x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 396 ms: 1.66x faster                                                  |
| async_tree_io            | 980 ms                                                 | 597 ms: 1.64x faster                                                  |
| chaos                    | 65.8 ms                                                | 40.8 ms: 1.61x faster                                                 |
| scimark_lu               | 103 ms                                                 | 65.4 ms: 1.57x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 179 us: 1.57x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.54x faster                                                 |
| mako                     | 9.87 ms                                                | 6.51 ms: 1.52x faster                                                 |
| go                       | 151 ms                                                 | 102 ms: 1.48x faster                                                  |
| float                    | 69.0 ms                                                | 46.6 ms: 1.48x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 131 us: 1.48x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.01 us: 1.48x faster                                                 |
| nbody                    | 93.0 ms                                                | 63.5 ms: 1.47x faster                                                 |
| logging_format           | 4.83 us                                                | 3.30 us: 1.46x faster                                                 |
| scimark_sor              | 128 ms                                                 | 88.3 ms: 1.45x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 858 us: 1.45x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 67.9 ms: 1.40x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 470 ms: 1.38x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 52.1 ms: 1.38x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.05 ms: 1.38x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.24 sec: 1.37x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 34.6 ms: 1.34x faster                                                 |
| thrift                   | 572 us                                                 | 428 us: 1.34x faster                                                  |
| pylint                   | 277 ms                                                 | 208 ms: 1.33x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 49.5 ms: 1.32x faster                                                 |
| generators               | 32.3 ms                                                | 24.4 ms: 1.32x faster                                                 |
| comprehensions           | 16.9 us                                                | 12.9 us: 1.32x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.76 ms: 1.30x faster                                                 |
| html5lib                 | 42.4 ms                                                | 32.8 ms: 1.29x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.29x faster                                                 |
| pyflate                  | 427 ms                                                 | 331 ms: 1.29x faster                                                  |
| pycparser                | 877 ms                                                 | 685 ms: 1.28x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 501 ms: 1.28x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.36 ms: 1.27x faster                                                 |
| regex_compile            | 95.3 ms                                                | 74.9 ms: 1.27x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 1.03 sec: 1.26x faster                                                |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.25x faster                                                |
| dulwich_log              | 35.3 ms                                                | 29.0 ms: 1.22x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 76.3 ms: 1.21x faster                                                 |
| richards_super           | 57.8 ms                                                | 48.1 ms: 1.20x faster                                                 |
| regex_dna                | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| scimark_fft              | 224 ms                                                 | 192 ms: 1.17x faster                                                  |
| sympy_str                | 165 ms                                                 | 145 ms: 1.14x faster                                                  |
| django_template          | 26.4 ms                                                | 23.2 ms: 1.14x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 11.7 ms: 1.12x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.46 sec: 1.12x faster                                                |
| fannkuch                 | 303 ms                                                 | 271 ms: 1.12x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 473 us: 1.11x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.57 sec: 1.10x faster                                                |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.11 ms: 1.10x faster                                                 |
| nqueens                  | 63.8 ms                                                | 58.4 ms: 1.09x faster                                                 |
| 2to3                     | 192 ms                                                 | 178 ms: 1.08x faster                                                  |
| sympy_expand             | 269 ms                                                 | 252 ms: 1.07x faster                                                  |
| richards                 | 48.7 ms                                                | 46.1 ms: 1.06x faster                                                 |
| json                     | 3.08 ms                                                | 2.95 ms: 1.05x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 51.3 ms: 1.04x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 75.0 ms: 1.04x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.7 ms: 1.03x faster                                                 |
| genshi_text              | 17.3 ms                                                | 16.8 ms: 1.03x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 185 ms: 1.03x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 36.1 ms: 1.02x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.47 ms: 1.00x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 904 us: 1.05x slower                                                  |
| pickle                   | 6.97 us                                                | 7.39 us: 1.06x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.37 us: 1.07x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.91 us: 1.08x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.96 us: 1.08x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.0 ms: 1.08x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.58 us: 1.09x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 41.6 ms: 1.23x slower                                                 |
| async_generators         | 231 ms                                                 | 295 ms: 1.28x slower                                                  |
| telco                    | 3.49 ms                                                | 4.71 ms: 1.35x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 52.0 ms: 1.39x slower                                                 |
| python_startup           | 10.9 ms                                                | 17.1 ms: 1.57x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 14.1 ms: 1.78x slower                                                 |
| unpack_sequence          | 39.0 ns                                                | 75.8 ns: 1.94x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_iterparse, pidigits, xml_etree_parse, tornado_http
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.226x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 0.52x