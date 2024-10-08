# Results vs. 3.10.4

- fork: brandtbucher
- ref: trace_through
- machine: linux-x86_64
- commit hash: b1a2c42
- commit date: 2024-09-06
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 278 ms: 1.25x faster                                                 |
| docutils       | 3.30 sec                                               | 3.00 sec: 1.10x faster                                               |
| html5lib       | 88.9 ms                                                | 62.4 ms: 1.42x faster                                                |
| tornado_http   | 136 ms                                                 | 95.7 ms: 1.42x faster                                                |
| Geometric mean | (ref)                                                  | 1.29x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 402 ms: 2.17x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 926 ms: 1.91x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 562 ms: 1.81x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.0 ms: 1.90x faster                                                |
| float          | 117 ms                                                 | 70.3 ms: 1.67x faster                                                |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.48x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 145 ms: 1.30x faster                                                 |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.47 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                  | 1.13x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                               |
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 54.0 ms: 1.47x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 76.5 ms: 1.30x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                 |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                |
| unpickle             | 14.4 us                                                | 15.3 us: 1.06x slower                                                |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                |
| pickle_dict          | 29.6 us                                                | 34.5 us: 1.17x slower                                                |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                         |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.85 ms: 1.66x faster                                                |
| django_template | 48.2 ms                                                | 36.6 ms: 1.32x faster                                                |
| genshi_text     | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                |
| genshi_xml      | 66.0 ms                                                | 55.9 ms: 1.18x faster                                                |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.11 ms: 2.55x faster                                                |
| generators               | 80.1 ms                                                | 33.0 ms: 2.43x faster                                                |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 26.4 us: 2.22x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 402 ms: 2.17x faster                                                 |
| richards_super           | 94.7 ms                                                | 44.0 ms: 2.15x faster                                                |
| richards                 | 79.3 ms                                                | 39.8 ms: 1.99x faster                                                |
| chaos                    | 115 ms                                                 | 58.7 ms: 1.97x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 66.7 ms: 1.92x faster                                                |
| async_tree_io            | 1.77 sec                                               | 926 ms: 1.91x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 485 ms: 1.90x faster                                                 |
| logging_silent           | 190 ns                                                 | 100.0 ns: 1.90x faster                                               |
| nbody                    | 154 ms                                                 | 81.0 ms: 1.90x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 62.7 ms: 1.89x faster                                                |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.89x faster                                                 |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                 |
| deepcopy                 | 479 us                                                 | 264 us: 1.81x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 562 ms: 1.81x faster                                                 |
| go                       | 240 ms                                                 | 134 ms: 1.79x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.69x faster                                                 |
| float                    | 117 ms                                                 | 70.3 ms: 1.67x faster                                                |
| mako                     | 16.3 ms                                                | 9.85 ms: 1.66x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                               |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                 |
| pyflate                  | 716 ms                                                 | 449 ms: 1.60x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.62 us: 1.59x faster                                                |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.55x faster                                                |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                                |
| pylint                   | 551 ms                                                 | 374 ms: 1.47x faster                                                 |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.47x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 54.0 ms: 1.47x faster                                                |
| logging_simple           | 8.30 us                                                | 5.67 us: 1.46x faster                                                |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.43 ms: 1.46x faster                                                |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                               |
| tornado_http             | 136 ms                                                 | 95.7 ms: 1.42x faster                                                |
| html5lib                 | 88.9 ms                                                | 62.4 ms: 1.42x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 716 ms: 1.42x faster                                                 |
| fannkuch                 | 532 ms                                                 | 374 ms: 1.42x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                               |
| thrift                   | 1.07 ms                                                | 780 us: 1.37x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                |
| hexiom                   | 10.4 ms                                                | 7.73 ms: 1.34x faster                                                |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                               |
| django_template          | 48.2 ms                                                | 36.6 ms: 1.32x faster                                                |
| regex_compile            | 188 ms                                                 | 145 ms: 1.30x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 76.5 ms: 1.30x faster                                                |
| genshi_text              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                 |
| 2to3                     | 348 ms                                                 | 278 ms: 1.25x faster                                                 |
| nqueens                  | 106 ms                                                 | 86.1 ms: 1.23x faster                                                |
| dulwich_log              | 84.3 ms                                                | 70.7 ms: 1.19x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 58.4 ms: 1.19x faster                                                |
| bench_thread_pool        | 986 us                                                 | 834 us: 1.18x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 55.9 ms: 1.18x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                |
| sympy_str                | 346 ms                                                 | 304 ms: 1.14x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 23.0 ms: 1.12x faster                                                |
| sympy_sum                | 196 ms                                                 | 175 ms: 1.12x faster                                                 |
| sympy_expand             | 566 ms                                                 | 507 ms: 1.12x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                                |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                 |
| docutils                 | 3.30 sec                                               | 3.00 sec: 1.10x faster                                               |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                                |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.72 sec: 1.05x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.47 ms: 1.05x faster                                                |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| gc_traversal             | 3.62 ms                                                | 3.59 ms: 1.01x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                 |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                                 |
| unpickle                 | 14.4 us                                                | 15.3 us: 1.06x slower                                                |
| coverage                 | 79.4 ms                                                | 85.8 ms: 1.08x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                |
| telco                    | 7.27 ms                                                | 7.99 ms: 1.10x slower                                                |
| pickle_dict              | 29.6 us                                                | 34.5 us: 1.17x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                |
| unpack_sequence          | 60.0 ns                                                | 139 ns: 2.31x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                         |

Benchmark hidden because not significant (3): unpickle_list, bench_mp_pool, pickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240906-3.14.0a0-b1a2c42-JIT/bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.23x