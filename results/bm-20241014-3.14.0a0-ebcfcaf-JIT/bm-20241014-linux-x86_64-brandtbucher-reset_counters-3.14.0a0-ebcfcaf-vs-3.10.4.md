# Results vs. 3.10.4

- fork: brandtbucher
- ref: reset_counters
- machine: linux-x86_64
- commit hash: ebcfcaf
- commit date: 2024-10-14
- overall geometric mean: 1.394x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 278 ms: 1.25x faster                                                  |
| docutils       | 3.30 sec                                               | 2.87 sec: 1.15x faster                                                |
| html5lib       | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                 |
| tornado_http   | 136 ms                                                 | 93.7 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 83.5 ms: 1.84x faster                                                 |
| float          | 117 ms                                                 | 72.4 ms: 1.62x faster                                                 |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.45x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.36x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                 |
| regex_dna      | 227 ms                                                 | 209 ms: 1.09x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                |
| pickle_pure_python   | 484 us                                                 | 310 us: 1.57x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 54.9 ms: 1.44x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 78.4 ms: 1.27x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 98.0 ms: 1.18x faster                                                 |
| json_loads           | 31.2 us                                                | 26.6 us: 1.17x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.17 us: 1.02x slower                                                 |
| unpickle             | 14.4 us                                                | 14.8 us: 1.03x slower                                                 |
| unpickle_list        | 5.20 us                                                | 5.41 us: 1.04x slower                                                 |
| pickle               | 10.7 us                                                | 11.8 us: 1.10x slower                                                 |
| pickle_dict          | 29.6 us                                                | 35.2 us: 1.19x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                 |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                 |
| genshi_text     | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 58.0 ms: 1.14x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                 |
| generators               | 80.1 ms                                                | 35.3 ms: 2.27x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 27.4 us: 2.13x faster                                                 |
| richards_super           | 94.7 ms                                                | 45.2 ms: 2.10x faster                                                 |
| chaos                    | 115 ms                                                 | 59.1 ms: 1.95x faster                                                 |
| richards                 | 79.3 ms                                                | 40.7 ms: 1.95x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 66.7 ms: 1.92x faster                                                 |
| logging_silent           | 190 ns                                                 | 99.8 ns: 1.90x faster                                                 |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 63.5 ms: 1.86x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 496 ms: 1.86x faster                                                  |
| nbody                    | 154 ms                                                 | 83.5 ms: 1.84x faster                                                 |
| deepcopy                 | 479 us                                                 | 264 us: 1.82x faster                                                  |
| go                       | 240 ms                                                 | 132 ms: 1.81x faster                                                  |
| raytrace                 | 507 ms                                                 | 282 ms: 1.80x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.71x faster                                                 |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.67x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                 |
| float                    | 117 ms                                                 | 72.4 ms: 1.62x faster                                                 |
| pyflate                  | 716 ms                                                 | 447 ms: 1.60x faster                                                  |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 310 us: 1.57x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.54x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.48 us: 1.51x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                 |
| logging_format           | 9.09 us                                                | 6.04 us: 1.51x faster                                                 |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                  |
| hexiom                   | 10.4 ms                                                | 7.00 ms: 1.49x faster                                                 |
| pylint                   | 551 ms                                                 | 373 ms: 1.48x faster                                                  |
| tornado_http             | 136 ms                                                 | 93.7 ms: 1.45x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 54.9 ms: 1.44x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                |
| html5lib                 | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.62 ms: 1.40x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 728 ms: 1.40x faster                                                  |
| fannkuch                 | 532 ms                                                 | 381 ms: 1.40x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                |
| thrift                   | 1.07 ms                                                | 785 us: 1.36x faster                                                  |
| regex_compile            | 188 ms                                                 | 139 ms: 1.36x faster                                                  |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                 |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 78.4 ms: 1.27x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                 |
| genshi_text              | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                 |
| 2to3                     | 348 ms                                                 | 278 ms: 1.25x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 67.5 ms: 1.25x faster                                                 |
| nqueens                  | 106 ms                                                 | 86.5 ms: 1.22x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.0 ms: 1.18x faster                                                 |
| json_loads               | 31.2 us                                                | 26.6 us: 1.17x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 59.3 ms: 1.17x faster                                                 |
| json                     | 5.69 ms                                                | 4.93 ms: 1.15x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.87 sec: 1.15x faster                                                |
| genshi_xml               | 66.0 ms                                                | 58.0 ms: 1.14x faster                                                 |
| sympy_expand             | 566 ms                                                 | 498 ms: 1.13x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 871 us: 1.13x faster                                                  |
| sympy_sum                | 196 ms                                                 | 175 ms: 1.13x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                                |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 23.2 ms: 1.11x faster                                                 |
| regex_dna                | 227 ms                                                 | 209 ms: 1.09x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                                 |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                  |
| pickle_list              | 5.08 us                                                | 5.17 us: 1.02x slower                                                 |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                  |
| unpickle                 | 14.4 us                                                | 14.8 us: 1.03x slower                                                 |
| unpickle_list            | 5.20 us                                                | 5.41 us: 1.04x slower                                                 |
| telco                    | 7.27 ms                                                | 7.62 ms: 1.05x slower                                                 |
| coverage                 | 79.4 ms                                                | 83.5 ms: 1.05x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                 |
| pickle                   | 10.7 us                                                | 11.8 us: 1.10x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.01 ms: 1.11x slower                                                 |
| pickle_dict              | 29.6 us                                                | 35.2 us: 1.19x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| unpack_sequence          | 60.0 ns                                                | 112 ns: 1.86x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 60.8 ms: 2.53x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20241014-3.14.0a0-ebcfcaf-JIT/bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf.json: bpe_tokeniser

- Geometric mean (including insignificant results): 1.394x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.21x