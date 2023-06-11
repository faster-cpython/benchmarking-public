
# Results vs. 3.10.4

- fork: brandtbucher
- ref: clean_up_calls
- machine: linux-x86_64
- commit hash: 28adc90
- commit date: 2023-06-10
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.70 sec: 1.17x faster                                                |
| tornado_http   | 127 ms                                                 | 98.6 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.1 ms: 1.59x faster                                                 |
| float          | 111 ms                                                 | 79.4 ms: 1.39x faster                                                 |
| pidigits       | 190 ms                                                 | 196 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 141 ms: 1.26x faster                                                  |
| regex_v8       | 25.0 ms                                                | 23.0 ms: 1.09x faster                                                 |
| regex_dna      | 222 ms                                                 | 216 ms: 1.03x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.64 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 313 us: 1.46x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 213 us: 1.41x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.72 ms: 1.39x faster                                                 |
| tomli_loads          | 2.92 sec                                               | 2.18 sec: 1.34x faster                                                |
| xml_etree_process    | 74.9 ms                                                | 58.2 ms: 1.29x faster                                                 |
| json_loads           | 28.8 us                                                | 25.3 us: 1.14x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 84.3 ms: 1.12x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.63 us: 1.02x slower                                                 |
| unpickle_list        | 4.82 us                                                | 4.96 us: 1.03x slower                                                 |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                                 |
| unpickle             | 14.1 us                                                | 15.2 us: 1.08x slower                                                 |
| pickle_dict          | 27.3 us                                                | 30.2 us: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.17 ms: 1.54x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.66 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.37x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 143 us: 3.57x faster                                                  |
| generators               | 76.8 ms                                                | 28.6 ms: 2.68x faster                                                 |
| deltablue                | 7.42 ms                                                | 3.24 ms: 2.29x faster                                                 |
| asyncio_tcp              | 925 ms                                                 | 516 ms: 1.79x faster                                                  |
| richards_super           | 90.7 ms                                                | 50.8 ms: 1.79x faster                                                 |
| logging_silent           | 175 ns                                                 | 98.3 ns: 1.78x faster                                                 |
| chaos                    | 106 ms                                                 | 62.4 ms: 1.70x faster                                                 |
| go                       | 229 ms                                                 | 136 ms: 1.69x faster                                                  |
| richards                 | 74.9 ms                                                | 44.5 ms: 1.68x faster                                                 |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.67x faster                                                |
| scimark_sor              | 197 ms                                                 | 118 ms: 1.67x faster                                                  |
| nbody                    | 142 ms                                                 | 89.1 ms: 1.59x faster                                                 |
| raytrace                 | 464 ms                                                 | 294 ms: 1.58x faster                                                  |
| hexiom                   | 9.53 ms                                                | 6.05 ms: 1.57x faster                                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.32 ms: 1.56x faster                                                 |
| python_startup           | 14.2 ms                                                | 9.17 ms: 1.54x faster                                                 |
| crypto_pyaes             | 118 ms                                                 | 77.2 ms: 1.53x faster                                                 |
| scimark_monte_carlo      | 108 ms                                                 | 70.9 ms: 1.53x faster                                                 |
| spectral_norm            | 150 ms                                                 | 99.2 ms: 1.51x faster                                                 |
| pyflate                  | 673 ms                                                 | 446 ms: 1.51x faster                                                  |
| sqlglot_transpile        | 2.45 ms                                                | 1.63 ms: 1.50x faster                                                 |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.47x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 1.21 sec: 1.46x faster                                                |
| pickle_pure_python       | 455 us                                                 | 313 us: 1.46x faster                                                  |
| coroutines               | 31.8 ms                                                | 22.0 ms: 1.44x faster                                                 |
| async_tree_none          | 717 ms                                                 | 497 ms: 1.44x faster                                                  |
| async_tree_memoization   | 854 ms                                                 | 604 ms: 1.41x faster                                                  |
| unpickle_pure_python     | 300 us                                                 | 213 us: 1.41x faster                                                  |
| json_dumps               | 13.5 ms                                                | 9.72 ms: 1.39x faster                                                 |
| float                    | 111 ms                                                 | 79.4 ms: 1.39x faster                                                 |
| deepcopy_memo            | 52.3 us                                                | 37.7 us: 1.39x faster                                                 |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.37x faster                                                 |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                |
| tomli_loads              | 2.92 sec                                               | 2.18 sec: 1.34x faster                                                |
| unpack_sequence          | 64.7 ns                                                | 48.5 ns: 1.34x faster                                                 |
| logging_simple           | 8.07 us                                                | 6.06 us: 1.33x faster                                                 |
| pprint_safe_repr         | 955 ms                                                 | 722 ms: 1.32x faster                                                  |
| comprehensions           | 26.8 us                                                | 20.4 us: 1.31x faster                                                 |
| logging_format           | 8.91 us                                                | 6.80 us: 1.31x faster                                                 |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                |
| tornado_http             | 127 ms                                                 | 98.6 ms: 1.29x faster                                                 |
| xml_etree_process        | 74.9 ms                                                | 58.2 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 739 ms: 1.29x faster                                                  |
| nqueens                  | 100 ms                                                 | 78.7 ms: 1.27x faster                                                 |
| fannkuch                 | 486 ms                                                 | 384 ms: 1.26x faster                                                  |
| sqlglot_normalize        | 135 ms                                                 | 107 ms: 1.26x faster                                                  |
| regex_compile            | 177 ms                                                 | 141 ms: 1.26x faster                                                  |
| mypy2                    | 428 ms                                                 | 342 ms: 1.25x faster                                                  |
| deepcopy                 | 442 us                                                 | 354 us: 1.25x faster                                                  |
| scimark_fft              | 424 ms                                                 | 343 ms: 1.23x faster                                                  |
| sqlglot_optimize         | 65.3 ms                                                | 53.5 ms: 1.22x faster                                                 |
| deepcopy_reduce          | 3.82 us                                                | 3.18 us: 1.20x faster                                                 |
| docutils                 | 3.17 sec                                               | 2.70 sec: 1.17x faster                                                |
| bench_thread_pool        | 947 us                                                 | 826 us: 1.15x faster                                                  |
| json_loads               | 28.8 us                                                | 25.3 us: 1.14x faster                                                 |
| dulwich_log              | 75.9 ms                                                | 66.7 ms: 1.14x faster                                                 |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.84 ms: 1.13x faster                                                 |
| json                     | 5.42 ms                                                | 4.81 ms: 1.12x faster                                                 |
| mdp                      | 2.82 sec                                               | 2.52 sec: 1.12x faster                                                |
| create_gc_cycles         | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                 |
| xml_etree_generate       | 94.2 ms                                                | 84.3 ms: 1.12x faster                                                 |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                                  |
| regex_v8                 | 25.0 ms                                                | 23.0 ms: 1.09x faster                                                 |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                                 |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                                 |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                                  |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                                  |
| regex_dna                | 222 ms                                                 | 216 ms: 1.03x faster                                                  |
| pickle_list              | 4.56 us                                                | 4.63 us: 1.02x slower                                                 |
| unpickle_list            | 4.82 us                                                | 4.96 us: 1.03x slower                                                 |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                                 |
| pidigits                 | 190 ms                                                 | 196 ms: 1.03x slower                                                  |
| async_generators         | 425 ms                                                 | 443 ms: 1.04x slower                                                  |
| gc_traversal             | 3.84 ms                                                | 4.08 ms: 1.06x slower                                                 |
| telco                    | 6.54 ms                                                | 6.99 ms: 1.07x slower                                                 |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.08x slower                                                 |
| pickle_dict              | 27.3 us                                                | 30.2 us: 1.11x slower                                                 |
| regex_effbot             | 3.23 ms                                                | 3.64 ms: 1.13x slower                                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.66 ms: 1.14x slower                                                 |
| dask                     | 423 ms                                                 | 527 ms: 1.25x slower                                                  |
| coverage                 | 72.8 ms                                                | 94.9 ms: 1.30x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
