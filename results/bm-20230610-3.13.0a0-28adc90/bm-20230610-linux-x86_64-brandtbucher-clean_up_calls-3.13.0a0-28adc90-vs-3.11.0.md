
# Results vs. 3.11.0

- fork: brandtbucher
- ref: clean_up_calls
- machine: linux-x86_64
- commit hash: 28adc90
- commit date: 2023-06-10
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.70 sec: 1.03x slower                                                |
| tornado_http   | 96.3 ms                                                | 98.6 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.1 ms: 1.05x faster                                                 |
| pidigits       | 198 ms                                                 | 196 ms: 1.01x faster                                                  |
| float          | 77.2 ms                                                | 79.4 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.64 ms: 1.10x faster                                                 |
| regex_compile  | 138 ms                                                 | 141 ms: 1.02x slower                                                  |
| regex_v8       | 22.0 ms                                                | 23.0 ms: 1.04x slower                                                 |
| regex_dna      | 204 ms                                                 | 216 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.72 ms: 1.30x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 213 us: 1.07x faster                                                  |
| json_loads           | 26.5 us                                                | 25.3 us: 1.05x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                                  |
| pickle_dict          | 31.1 us                                                | 30.2 us: 1.03x faster                                                 |
| tomli_loads          | 2.22 sec                                               | 2.18 sec: 1.02x faster                                                |
| unpickle_list        | 4.91 us                                                | 4.96 us: 1.01x slower                                                 |
| pickle_pure_python   | 306 us                                                 | 313 us: 1.02x slower                                                  |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                                 |
| xml_etree_process    | 53.9 ms                                                | 58.2 ms: 1.08x slower                                                 |
| xml_etree_generate   | 76.2 ms                                                | 84.3 ms: 1.11x slower                                                 |
| unpickle             | 13.7 us                                                | 15.2 us: 1.11x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.63 us: 1.13x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.17 ms: 1.08x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.66 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 143 us: 3.40x faster                                                  |
| generators               | 73.5 ms                                                | 28.6 ms: 2.57x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 516 ms: 1.79x faster                                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                |
| json_dumps               | 12.6 ms                                                | 9.72 ms: 1.30x faster                                                 |
| mypy2                    | 420 ms                                                 | 342 ms: 1.23x faster                                                  |
| coroutines               | 25.5 ms                                                | 22.0 ms: 1.16x faster                                                 |
| deltablue                | 3.67 ms                                                | 3.24 ms: 1.13x faster                                                 |
| richards_super           | 56.8 ms                                                | 50.8 ms: 1.12x faster                                                 |
| chaos                    | 69.2 ms                                                | 62.4 ms: 1.11x faster                                                 |
| comprehensions           | 22.4 us                                                | 20.4 us: 1.10x faster                                                 |
| regex_effbot             | 3.99 ms                                                | 3.64 ms: 1.10x faster                                                 |
| unpickle_pure_python     | 228 us                                                 | 213 us: 1.07x faster                                                  |
| async_tree_io            | 1.30 sec                                               | 1.21 sec: 1.07x faster                                                |
| sqlglot_parse            | 1.40 ms                                                | 1.32 ms: 1.06x faster                                                 |
| async_tree_none          | 526 ms                                                 | 497 ms: 1.06x faster                                                  |
| nqueens                  | 83.4 ms                                                | 78.7 ms: 1.06x faster                                                 |
| coverage                 | 100 ms                                                 | 94.9 ms: 1.05x faster                                                 |
| hexiom                   | 6.37 ms                                                | 6.05 ms: 1.05x faster                                                 |
| json_loads               | 26.5 us                                                | 25.3 us: 1.05x faster                                                 |
| nbody                    | 93.1 ms                                                | 89.1 ms: 1.05x faster                                                 |
| sqlglot_transpile        | 1.70 ms                                                | 1.63 ms: 1.04x faster                                                 |
| mdp                      | 2.62 sec                                               | 2.52 sec: 1.04x faster                                                |
| async_tree_memoization   | 627 ms                                                 | 604 ms: 1.04x faster                                                  |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                                  |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                                  |
| pickle_dict              | 31.1 us                                                | 30.2 us: 1.03x faster                                                 |
| richards                 | 45.7 ms                                                | 44.5 ms: 1.03x faster                                                 |
| logging_silent           | 101 ns                                                 | 98.3 ns: 1.03x faster                                                 |
| json                     | 4.94 ms                                                | 4.81 ms: 1.03x faster                                                 |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                |
| tomli_loads              | 2.22 sec                                               | 2.18 sec: 1.02x faster                                                |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.01x faster                                                  |
| raytrace                 | 297 ms                                                 | 294 ms: 1.01x faster                                                  |
| fannkuch                 | 388 ms                                                 | 384 ms: 1.01x faster                                                  |
| spectral_norm            | 100 ms                                                 | 99.2 ms: 1.01x faster                                                 |
| pidigits                 | 198 ms                                                 | 196 ms: 1.01x faster                                                  |
| sqlglot_normalize        | 108 ms                                                 | 107 ms: 1.00x faster                                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.49 ms: 1.00x slower                                                 |
| logging_simple           | 6.03 us                                                | 6.06 us: 1.01x slower                                                 |
| sqlglot_optimize         | 53.1 ms                                                | 53.5 ms: 1.01x slower                                                 |
| bench_thread_pool        | 819 us                                                 | 826 us: 1.01x slower                                                  |
| unpickle_list            | 4.91 us                                                | 4.96 us: 1.01x slower                                                 |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                                |
| scimark_lu               | 110 ms                                                 | 111 ms: 1.01x slower                                                  |
| gc_traversal             | 4.02 ms                                                | 4.08 ms: 1.01x slower                                                 |
| logging_format           | 6.68 us                                                | 6.80 us: 1.02x slower                                                 |
| regex_compile            | 138 ms                                                 | 141 ms: 1.02x slower                                                  |
| deepcopy_memo            | 37.0 us                                                | 37.7 us: 1.02x slower                                                 |
| pickle_pure_python       | 306 us                                                 | 313 us: 1.02x slower                                                  |
| pathlib                  | 18.2 ms                                                | 18.7 ms: 1.02x slower                                                 |
| tornado_http             | 96.3 ms                                                | 98.6 ms: 1.02x slower                                                 |
| float                    | 77.2 ms                                                | 79.4 ms: 1.03x slower                                                 |
| docutils                 | 2.63 sec                                               | 2.70 sec: 1.03x slower                                                |
| pprint_safe_repr         | 701 ms                                                 | 722 ms: 1.03x slower                                                  |
| crypto_pyaes             | 74.7 ms                                                | 77.2 ms: 1.03x slower                                                 |
| deepcopy                 | 342 us                                                 | 354 us: 1.04x slower                                                  |
| scimark_monte_carlo      | 68.1 ms                                                | 70.9 ms: 1.04x slower                                                 |
| regex_v8                 | 22.0 ms                                                | 23.0 ms: 1.04x slower                                                 |
| scimark_fft              | 328 ms                                                 | 343 ms: 1.04x slower                                                  |
| dulwich_log              | 63.7 ms                                                | 66.7 ms: 1.05x slower                                                 |
| pickle                   | 10.1 us                                                | 10.6 us: 1.05x slower                                                 |
| regex_dna                | 204 ms                                                 | 216 ms: 1.06x slower                                                  |
| telco                    | 6.58 ms                                                | 6.99 ms: 1.06x slower                                                 |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                 |
| pyflate                  | 418 ms                                                 | 446 ms: 1.07x slower                                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.84 ms: 1.08x slower                                                 |
| python_startup           | 8.52 ms                                                | 9.17 ms: 1.08x slower                                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.18 us: 1.08x slower                                                 |
| xml_etree_process        | 53.9 ms                                                | 58.2 ms: 1.08x slower                                                 |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                                 |
| xml_etree_generate       | 76.2 ms                                                | 84.3 ms: 1.11x slower                                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.66 ms: 1.11x slower                                                 |
| unpickle                 | 13.7 us                                                | 15.2 us: 1.11x slower                                                 |
| unpack_sequence          | 43.1 ns                                                | 48.5 ns: 1.12x slower                                                 |
| pickle_list              | 4.11 us                                                | 4.63 us: 1.13x slower                                                 |
| async_generators         | 368 ms                                                 | 443 ms: 1.20x slower                                                  |
| dask                     | 360 ms                                                 | 527 ms: 1.46x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (4): scimark_sor, bench_mp_pool, async_tree_cpu_io_mixed, xml_etree_iterparse
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
