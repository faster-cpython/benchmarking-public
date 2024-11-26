# Results vs. 3.10.4

- fork: brandtbucher
- ref: optimize_off
- machine: linux-x86_64
- commit hash: 9808234
- commit date: 2024-11-17
- overall geometric mean: 1.373x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 283 ms: 1.23x faster                                                 |
| docutils       | 3.30 sec                                               | 3.13 sec: 1.05x faster                                               |
| html5lib       | 88.9 ms                                                | 68.6 ms: 1.30x faster                                                |
| Geometric mean | (ref)                                                  | 1.19x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 333 ms: 2.19x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 421 ms: 2.07x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 858 ms: 2.06x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 577 ms: 1.76x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 84.5 ms: 1.82x faster                                                |
| float          | 117 ms                                                 | 77.2 ms: 1.52x faster                                                |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.41x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                                 |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.73 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.64x faster                                               |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 328 us: 1.47x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 78.7 ms: 1.26x faster                                                |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                |
| json_loads           | 31.2 us                                                | 26.6 us: 1.17x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 99.7 ms: 1.16x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.3 ms: 1.58x faster                                                |
| django_template | 48.2 ms                                                | 34.3 ms: 1.40x faster                                                |
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                |
| genshi_xml      | 66.0 ms                                                | 60.8 ms: 1.09x faster                                                |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.39 ms: 2.33x faster                                                |
| generators               | 80.1 ms                                                | 36.4 ms: 2.20x faster                                                |
| async_tree_none          | 728 ms                                                 | 333 ms: 2.19x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 421 ms: 2.07x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 858 ms: 2.06x faster                                                 |
| richards                 | 79.3 ms                                                | 39.7 ms: 2.00x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                |
| richards_super           | 94.7 ms                                                | 48.2 ms: 1.96x faster                                                |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                 |
| chaos                    | 115 ms                                                 | 61.5 ms: 1.88x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 69.1 ms: 1.85x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 64.6 ms: 1.83x faster                                                |
| nbody                    | 154 ms                                                 | 84.5 ms: 1.82x faster                                                |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                 |
| go                       | 240 ms                                                 | 136 ms: 1.77x faster                                                 |
| deepcopy                 | 479 us                                                 | 272 us: 1.76x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 577 ms: 1.76x faster                                                 |
| raytrace                 | 507 ms                                                 | 292 ms: 1.74x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.64x faster                                               |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                                |
| comprehensions           | 28.8 us                                                | 17.8 us: 1.61x faster                                                |
| mako                     | 16.3 ms                                                | 10.3 ms: 1.58x faster                                                |
| djangocms                | 38.4 us                                                | 24.3 us: 1.58x faster                                                |
| pyflate                  | 716 ms                                                 | 458 ms: 1.57x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                 |
| float                    | 117 ms                                                 | 77.2 ms: 1.52x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.72 ms: 1.49x faster                                                |
| pickle_pure_python       | 484 us                                                 | 328 us: 1.47x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                                |
| logging_format           | 9.09 us                                                | 6.24 us: 1.46x faster                                                |
| hexiom                   | 10.4 ms                                                | 7.19 ms: 1.45x faster                                                |
| scimark_fft              | 466 ms                                                 | 325 ms: 1.43x faster                                                 |
| pylint                   | 551 ms                                                 | 385 ms: 1.43x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                |
| django_template          | 48.2 ms                                                | 34.3 ms: 1.40x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.64 ms: 1.39x faster                                                |
| spectral_norm            | 170 ms                                                 | 122 ms: 1.39x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.37x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 747 ms: 1.36x faster                                                 |
| fannkuch                 | 532 ms                                                 | 390 ms: 1.36x faster                                                 |
| thrift                   | 1.07 ms                                                | 795 us: 1.35x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.7 ms: 1.32x faster                                                |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                               |
| html5lib                 | 88.9 ms                                                | 68.6 ms: 1.30x faster                                                |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 78.7 ms: 1.26x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 116 ms: 1.23x faster                                                 |
| 2to3                     | 348 ms                                                 | 283 ms: 1.23x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 68.6 ms: 1.23x faster                                                |
| json_loads               | 31.2 us                                                | 26.6 us: 1.17x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 147 ms: 1.17x faster                                                 |
| nqueens                  | 106 ms                                                 | 90.7 ms: 1.17x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 99.7 ms: 1.16x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 60.6 ms: 1.14x faster                                                |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| json                     | 5.69 ms                                                | 5.03 ms: 1.13x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                 |
| sympy_str                | 346 ms                                                 | 307 ms: 1.13x faster                                                 |
| sympy_expand             | 566 ms                                                 | 508 ms: 1.11x faster                                                 |
| sympy_sum                | 196 ms                                                 | 177 ms: 1.11x faster                                                 |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 895 us: 1.10x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                |
| genshi_xml               | 66.0 ms                                                | 60.8 ms: 1.09x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 23.8 ms: 1.08x faster                                                |
| mdp                      | 2.85 sec                                               | 2.63 sec: 1.08x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                 |
| docutils                 | 3.30 sec                                               | 3.13 sec: 1.05x faster                                               |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                 |
| telco                    | 7.27 ms                                                | 7.42 ms: 1.02x slower                                                |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.73 ms: 1.03x slower                                                |
| coverage                 | 79.4 ms                                                | 84.7 ms: 1.07x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.52 ms: 1.25x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.68 ms: 1.65x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 84.5 ms: 3.52x slower                                                |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                         |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241117-3.14.0a1+-9808234-JIT/bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.373x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.34x