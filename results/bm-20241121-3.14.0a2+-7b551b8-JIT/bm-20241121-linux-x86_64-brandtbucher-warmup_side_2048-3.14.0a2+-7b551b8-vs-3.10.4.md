# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_side_2048
- machine: linux-x86_64
- commit hash: 7b551b8
- commit date: 2024-11-21
- overall geometric mean: 1.411x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.33x faster                                                     |
| docutils       | 3.30 sec                                               | 2.79 sec: 1.18x faster                                                   |
| html5lib       | 88.9 ms                                                | 66.9 ms: 1.33x faster                                                    |
| Geometric mean | (ref)                                                  | 1.28x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 415 ms: 2.09x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 914 ms: 1.93x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 565 ms: 1.80x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.3 ms: 1.86x faster                                                    |
| float          | 117 ms                                                 | 77.8 ms: 1.51x faster                                                    |
| pidigits       | 191 ms                                                 | 191 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.41x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                     |
| regex_v8       | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                    |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.13x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 193 us: 1.72x faster                                                     |
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 316 us: 1.53x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 55.3 ms: 1.43x faster                                                    |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 78.5 ms: 1.27x faster                                                    |
| json_loads           | 31.2 us                                                | 26.3 us: 1.19x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.93 ms: 1.64x faster                                                    |
| django_template | 48.2 ms                                                | 33.4 ms: 1.44x faster                                                    |
| genshi_text     | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 59.1 ms: 1.12x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.23x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                    |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                                     |
| generators               | 80.1 ms                                                | 37.1 ms: 2.16x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 415 ms: 2.09x faster                                                     |
| richards_super           | 94.7 ms                                                | 45.8 ms: 2.07x faster                                                    |
| richards                 | 79.3 ms                                                | 39.4 ms: 2.01x faster                                                    |
| pylint                   | 551 ms                                                 | 275 ms: 2.01x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 2.00x faster                                                    |
| chaos                    | 115 ms                                                 | 59.3 ms: 1.95x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 914 ms: 1.93x faster                                                     |
| logging_silent           | 190 ns                                                 | 100 ns: 1.89x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 68.1 ms: 1.88x faster                                                    |
| nbody                    | 154 ms                                                 | 82.3 ms: 1.86x faster                                                    |
| go                       | 240 ms                                                 | 131 ms: 1.84x faster                                                     |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 65.3 ms: 1.81x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 565 ms: 1.80x faster                                                     |
| deepcopy                 | 479 us                                                 | 267 us: 1.80x faster                                                     |
| raytrace                 | 507 ms                                                 | 285 ms: 1.78x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 193 us: 1.72x faster                                                     |
| djangocms                | 38.4 us                                                | 22.6 us: 1.70x faster                                                    |
| mako                     | 16.3 ms                                                | 9.93 ms: 1.64x faster                                                    |
| pyflate                  | 716 ms                                                 | 439 ms: 1.63x faster                                                     |
| comprehensions           | 28.8 us                                                | 17.7 us: 1.63x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 316 us: 1.53x faster                                                     |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                    |
| float                    | 117 ms                                                 | 77.8 ms: 1.51x faster                                                    |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                    |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                                    |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.47x faster                                                     |
| hexiom                   | 10.4 ms                                                | 7.11 ms: 1.46x faster                                                    |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                     |
| django_template          | 48.2 ms                                                | 33.4 ms: 1.44x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 55.3 ms: 1.43x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.67 ms: 1.39x faster                                                    |
| fannkuch                 | 532 ms                                                 | 385 ms: 1.38x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                   |
| thrift                   | 1.07 ms                                                | 785 us: 1.36x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.3 ms: 1.35x faster                                                    |
| 2to3                     | 348 ms                                                 | 261 ms: 1.33x faster                                                     |
| html5lib                 | 88.9 ms                                                | 66.9 ms: 1.33x faster                                                    |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.33x faster                                                     |
| genshi_text              | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.29x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 78.5 ms: 1.27x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                    |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.25x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 67.4 ms: 1.25x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.25x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 55.7 ms: 1.24x faster                                                    |
| sympy_str                | 346 ms                                                 | 283 ms: 1.22x faster                                                     |
| nqueens                  | 106 ms                                                 | 87.9 ms: 1.20x faster                                                    |
| json_loads               | 31.2 us                                                | 26.3 us: 1.19x faster                                                    |
| json                     | 5.69 ms                                                | 4.80 ms: 1.18x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.79 sec: 1.18x faster                                                   |
| sympy_expand             | 566 ms                                                 | 480 ms: 1.18x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                     |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                    |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 873 us: 1.13x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 59.1 ms: 1.12x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                    |
| regex_effbot             | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.78 sec: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                     |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                     |
| pidigits                 | 191 ms                                                 | 191 ms: 1.00x faster                                                     |
| async_generators         | 444 ms                                                 | 455 ms: 1.02x slower                                                     |
| telco                    | 7.27 ms                                                | 7.63 ms: 1.05x slower                                                    |
| coverage                 | 79.4 ms                                                | 84.2 ms: 1.06x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.47 ms: 1.23x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 2.64 ms: 1.63x slower                                                    |
| bench_mp_pool            | 24.0 ms                                                | 79.4 ms: 3.31x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                             |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241121-3.14.0a2+-7b551b8-JIT/bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.411x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x