# Results vs. 3.12.0

- fork: brandtbucher
- ref: reset_counters
- machine: linux-x86_64
- commit hash: ebcfcaf
- commit date: 2024-10-14
- overall geometric mean: 1.056x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 278 ms: 1.01x slower                                                  |
| docutils       | 2.77 sec                                               | 2.87 sec: 1.04x slower                                                |
| tornado_http   | 103 ms                                                 | 93.7 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.4 ms: 1.17x faster                                                 |
| nbody          | 97.0 ms                                                | 83.5 ms: 1.16x faster                                                 |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.07x faster                                                  |
| regex_dna      | 212 ms                                                 | 209 ms: 1.02x faster                                                  |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 78.4 ms: 1.14x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 54.9 ms: 1.12x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 98.0 ms: 1.09x faster                                                 |
| json_loads           | 28.5 us                                                | 26.6 us: 1.07x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                  |
| unpickle             | 15.9 us                                                | 14.8 us: 1.07x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 310 us: 1.05x faster                                                  |
| pickle_dict          | 35.5 us                                                | 35.2 us: 1.01x faster                                                 |
| pickle               | 11.6 us                                                | 11.8 us: 1.01x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.17 us: 1.02x slower                                                 |
| unpickle_list        | 5.29 us                                                | 5.41 us: 1.02x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                 |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo            | 40.7 us                                                | 27.4 us: 1.49x faster                                                 |
| deepcopy                 | 371 us                                                 | 264 us: 1.41x faster                                                  |
| comprehensions           | 21.8 us                                                | 16.9 us: 1.29x faster                                                 |
| deepcopy_reduce          | 3.35 us                                                | 2.66 us: 1.26x faster                                                 |
| crypto_pyaes             | 81.9 ms                                                | 66.7 ms: 1.23x faster                                                 |
| scimark_fft              | 382 ms                                                 | 312 ms: 1.22x faster                                                  |
| tomli_loads              | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                |
| pathlib                  | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                 |
| logging_format           | 7.23 us                                                | 6.04 us: 1.20x faster                                                 |
| mako                     | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                 |
| scimark_monte_carlo      | 75.1 ms                                                | 63.5 ms: 1.18x faster                                                 |
| logging_simple           | 6.46 us                                                | 5.48 us: 1.18x faster                                                 |
| float                    | 84.7 ms                                                | 72.4 ms: 1.17x faster                                                 |
| nbody                    | 97.0 ms                                                | 83.5 ms: 1.16x faster                                                 |
| deltablue                | 3.72 ms                                                | 3.22 ms: 1.15x faster                                                 |
| richards_super           | 51.5 ms                                                | 45.2 ms: 1.14x faster                                                 |
| xml_etree_generate       | 89.2 ms                                                | 78.4 ms: 1.14x faster                                                 |
| chaos                    | 67.0 ms                                                | 59.1 ms: 1.13x faster                                                 |
| spectral_norm            | 115 ms                                                 | 101 ms: 1.13x faster                                                  |
| richards                 | 45.8 ms                                                | 40.7 ms: 1.13x faster                                                 |
| xml_etree_process        | 61.7 ms                                                | 54.9 ms: 1.12x faster                                                 |
| raytrace                 | 312 ms                                                 | 282 ms: 1.11x faster                                                  |
| scimark_sor              | 129 ms                                                 | 117 ms: 1.10x faster                                                  |
| fannkuch                 | 417 ms                                                 | 381 ms: 1.10x faster                                                  |
| xml_etree_parse          | 159 ms                                                 | 146 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult  | 5.06 ms                                                | 4.62 ms: 1.09x faster                                                 |
| tornado_http             | 103 ms                                                 | 93.7 ms: 1.09x faster                                                 |
| xml_etree_iterparse      | 107 ms                                                 | 98.0 ms: 1.09x faster                                                 |
| pyflate                  | 482 ms                                                 | 447 ms: 1.08x faster                                                  |
| json_loads               | 28.5 us                                                | 26.6 us: 1.07x faster                                                 |
| unpickle_pure_python     | 230 us                                                 | 215 us: 1.07x faster                                                  |
| unpickle                 | 15.9 us                                                | 14.8 us: 1.07x faster                                                 |
| scimark_lu               | 118 ms                                                 | 110 ms: 1.07x faster                                                  |
| regex_compile            | 148 ms                                                 | 139 ms: 1.07x faster                                                  |
| json                     | 5.26 ms                                                | 4.93 ms: 1.07x faster                                                 |
| pprint_safe_repr         | 776 ms                                                 | 728 ms: 1.07x faster                                                  |
| pprint_pformat           | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                |
| go                       | 139 ms                                                 | 132 ms: 1.05x faster                                                  |
| meteor_contest           | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| logging_silent           | 104 ns                                                 | 99.8 ns: 1.05x faster                                                 |
| pickle_pure_python       | 324 us                                                 | 310 us: 1.05x faster                                                  |
| sqlglot_parse            | 1.36 ms                                                | 1.32 ms: 1.04x faster                                                 |
| mdp                      | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                |
| async_generators         | 463 ms                                                 | 454 ms: 1.02x faster                                                  |
| regex_dna                | 212 ms                                                 | 209 ms: 1.02x faster                                                  |
| dulwich_log              | 68.5 ms                                                | 67.5 ms: 1.01x faster                                                 |
| sqlglot_transpile        | 1.68 ms                                                | 1.67 ms: 1.01x faster                                                 |
| pidigits                 | 187 ms                                                 | 185 ms: 1.01x faster                                                  |
| pickle_dict              | 35.5 us                                                | 35.2 us: 1.01x faster                                                 |
| asyncio_websockets       | 551 ms                                                 | 554 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl          | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| asyncio_tcp              | 491 ms                                                 | 496 ms: 1.01x slower                                                  |
| 2to3                     | 274 ms                                                 | 278 ms: 1.01x slower                                                  |
| pickle                   | 11.6 us                                                | 11.8 us: 1.01x slower                                                 |
| pickle_list              | 5.08 us                                                | 5.17 us: 1.02x slower                                                 |
| python_startup_no_site   | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                 |
| unpickle_list            | 5.29 us                                                | 5.41 us: 1.02x slower                                                 |
| sympy_sum                | 169 ms                                                 | 175 ms: 1.03x slower                                                  |
| sqlglot_normalize        | 110 ms                                                 | 114 ms: 1.03x slower                                                  |
| bench_thread_pool        | 842 us                                                 | 871 us: 1.03x slower                                                  |
| docutils                 | 2.77 sec                                               | 2.87 sec: 1.04x slower                                                |
| typing_runtime_protocols | 158 us                                                 | 164 us: 1.04x slower                                                  |
| nqueens                  | 83.3 ms                                                | 86.5 ms: 1.04x slower                                                 |
| django_template          | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                 |
| sympy_expand             | 478 ms                                                 | 498 ms: 1.04x slower                                                  |
| regex_v8                 | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                 |
| gc_traversal             | 3.79 ms                                                | 4.01 ms: 1.06x slower                                                 |
| telco                    | 7.10 ms                                                | 7.62 ms: 1.07x slower                                                 |
| json_dumps               | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| sqlglot_optimize         | 54.8 ms                                                | 59.3 ms: 1.08x slower                                                 |
| sympy_integrate          | 21.4 ms                                                | 23.2 ms: 1.08x slower                                                 |
| hexiom                   | 6.41 ms                                                | 7.00 ms: 1.09x slower                                                 |
| python_startup           | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| generators               | 31.2 ms                                                | 35.3 ms: 1.13x slower                                                 |
| coverage                 | 72.7 ms                                                | 83.5 ms: 1.15x slower                                                 |
| create_gc_cycles         | 1.48 ms                                                | 1.78 ms: 1.21x slower                                                 |
| unpack_sequence          | 54.0 ns                                                | 112 ns: 2.07x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 60.8 ms: 2.53x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (4): sqlite_synth, regex_effbot, sympy_str, coroutines
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241014-3.14.0a0-ebcfcaf-JIT/bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.056x faster
# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x