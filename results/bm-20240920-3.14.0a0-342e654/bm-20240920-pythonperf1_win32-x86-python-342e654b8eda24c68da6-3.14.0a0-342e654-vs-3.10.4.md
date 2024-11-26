# Results vs. 3.10.4

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-x86
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.124x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 256 ms: 1.04x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| html5lib       | 52.1 ms                                                         | 47.1 ms: 1.11x faster                                                          |
| tornado_http   | 118 ms                                                          | 95.6 ms: 1.23x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 475 ms: 1.94x faster                                                           |
| async_tree_none         | 394 ms                                                          | 223 ms: 1.77x faster                                                           |
| async_tree_io           | 940 ms                                                          | 544 ms: 1.73x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 277 ms: 1.68x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.55x faster                                                           |
| float          | 69.6 ms                                                         | 61.2 ms: 1.14x faster                                                          |
| nbody          | 79.1 ms                                                         | 91.0 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 110 ms: 1.06x faster                                                           |
| regex_dna      | 131 ms                                                          | 128 ms: 1.02x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.45 ms: 1.32x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 261 us: 1.07x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 177 us: 1.07x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.7 ms: 1.05x faster                                                          |
| json_loads           | 22.4 us                                                         | 21.5 us: 1.04x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 2.91 us: 1.02x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.92 sec: 1.01x slower                                                         |
| xml_etree_process    | 48.1 ms                                                         | 49.2 ms: 1.02x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.34 us: 1.04x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.04x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 67.3 ms: 1.09x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.6 us: 1.13x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.4 ms: 1.06x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.5 ms: 1.13x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.09 ms: 1.13x faster                                                          |
| django_template | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 48.5 ms: 1.04x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 22.5 ms: 1.07x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.02x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 144 us: 2.75x faster                                                           |
| pidigits                 | 502 ms                                                          | 197 ms: 2.55x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 475 ms: 1.94x faster                                                           |
| async_tree_none          | 394 ms                                                          | 223 ms: 1.77x faster                                                           |
| async_tree_io            | 940 ms                                                          | 544 ms: 1.73x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 277 ms: 1.68x faster                                                           |
| pylint                   | 384 ms                                                          | 234 ms: 1.64x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.73 ms: 1.48x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 59.8 ms: 1.36x faster                                                          |
| chaos                    | 74.4 ms                                                         | 55.1 ms: 1.35x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 21.9 us: 1.35x faster                                                          |
| go                       | 146 ms                                                          | 109 ms: 1.34x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.45 ms: 1.32x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 69.2 ms: 1.30x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 76.1 ns: 1.29x faster                                                          |
| deepcopy                 | 310 us                                                          | 243 us: 1.28x faster                                                           |
| comprehensions           | 17.7 us                                                         | 14.0 us: 1.27x faster                                                          |
| raytrace                 | 303 ms                                                          | 243 ms: 1.24x faster                                                           |
| tornado_http             | 118 ms                                                          | 95.6 ms: 1.23x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.09 ms: 1.22x faster                                                          |
| thrift                   | 902 us                                                          | 742 us: 1.22x faster                                                           |
| generators               | 31.6 ms                                                         | 26.2 ms: 1.20x faster                                                          |
| pycparser                | 1.04 sec                                                        | 880 ms: 1.18x faster                                                           |
| pyflate                  | 422 ms                                                          | 357 ms: 1.18x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.35 ms: 1.18x faster                                                          |
| scimark_sor              | 115 ms                                                          | 98.2 ms: 1.17x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.26 ms: 1.17x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.97 us: 1.16x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 644 ms: 1.15x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 75.6 ms: 1.15x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 51.1 ms: 1.15x faster                                                          |
| float                    | 69.6 ms                                                         | 61.2 ms: 1.14x faster                                                          |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.14x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.09 ms: 1.13x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 47.1 ms: 1.11x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                           |
| json                     | 4.76 ms                                                         | 4.34 ms: 1.10x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 56.7 ms: 1.09x faster                                                          |
| richards_super           | 49.9 ms                                                         | 45.9 ms: 1.09x faster                                                          |
| django_template          | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 261 us: 1.07x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 177 us: 1.07x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 75.8 ms: 1.06x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.53 us: 1.06x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.06 ms: 1.06x faster                                                          |
| regex_compile            | 117 ms                                                          | 110 ms: 1.06x faster                                                           |
| sympy_str                | 229 ms                                                          | 219 ms: 1.05x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.7 ms: 1.05x faster                                                          |
| json_loads               | 22.4 us                                                         | 21.5 us: 1.04x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| 2to3                     | 265 ms                                                          | 256 ms: 1.04x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.91 us: 1.02x faster                                                          |
| regex_dna                | 131 ms                                                          | 128 ms: 1.02x faster                                                           |
| sympy_expand             | 391 ms                                                          | 386 ms: 1.01x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 44.9 ms: 1.00x slower                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.92 sec: 1.01x slower                                                         |
| sqlglot_normalize        | 230 ms                                                          | 232 ms: 1.01x slower                                                           |
| richards                 | 40.3 ms                                                         | 40.6 ms: 1.01x slower                                                          |
| coroutines               | 17.9 ms                                                         | 18.1 ms: 1.01x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 49.2 ms: 1.02x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 83.2 ms: 1.02x slower                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.41 sec: 1.03x slower                                                         |
| pickle_list              | 3.22 us                                                         | 3.34 us: 1.04x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.04x slower                                                          |
| fannkuch                 | 317 ms                                                          | 330 ms: 1.04x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 48.5 ms: 1.04x slower                                                          |
| pprint_safe_repr         | 658 ms                                                          | 687 ms: 1.04x slower                                                           |
| python_startup           | 22.9 ms                                                         | 24.4 ms: 1.06x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 739 us: 1.07x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 22.5 ms: 1.07x slower                                                          |
| scimark_fft              | 216 ms                                                          | 236 ms: 1.09x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 67.3 ms: 1.09x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.02 us: 1.10x slower                                                          |
| coverage                 | 46.6 ms                                                         | 51.3 ms: 1.10x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.74 us: 1.11x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 74.4 ms: 1.12x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.6 us: 1.13x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 45.4 ns: 1.13x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.5 ms: 1.13x slower                                                          |
| nbody                    | 79.1 ms                                                         | 91.0 ms: 1.15x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| async_generators         | 241 ms                                                          | 300 ms: 1.25x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.53 ms: 1.35x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (4): mdp, asyncio_tcp_ssl, pickle, meteor_contest
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.124x faster
# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown