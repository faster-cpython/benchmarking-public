
# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: a4921c7
- commit date: 2023-07-16
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.71 sec: 1.17x faster                                        |
| tornado_http   | 127 ms                                                 | 98.7 ms: 1.29x faster                                         |
| Geometric mean | (ref)                                                  | 1.23x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 96.3 ms: 1.47x faster                                         |
| float          | 111 ms                                                 | 91.2 ms: 1.21x faster                                         |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.21x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 142 ms: 1.24x faster                                          |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                         |
| regex_dna      | 222 ms                                                 | 201 ms: 1.11x faster                                          |
| regex_effbot   | 3.23 ms                                                | 3.41 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 317 us: 1.43x faster                                          |
| json_dumps           | 13.5 ms                                                | 9.76 ms: 1.39x faster                                         |
| unpickle_pure_python | 300 us                                                 | 221 us: 1.36x faster                                          |
| xml_etree_process    | 74.9 ms                                                | 58.8 ms: 1.27x faster                                         |
| tomli_loads          | 2.92 sec                                               | 2.47 sec: 1.18x faster                                        |
| json_loads           | 28.8 us                                                | 24.9 us: 1.16x faster                                         |
| xml_etree_generate   | 94.2 ms                                                | 86.8 ms: 1.09x faster                                         |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                          |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.06x faster                                          |
| unpickle_list        | 4.82 us                                                | 4.86 us: 1.01x slower                                         |
| pickle_list          | 4.56 us                                                | 4.62 us: 1.01x slower                                         |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                         |
| unpickle             | 14.1 us                                                | 15.2 us: 1.08x slower                                         |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                         |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.48 ms: 1.49x faster                                         |
| python_startup_no_site | 5.82 ms                                                | 6.90 ms: 1.19x slower                                         |
| Geometric mean         | (ref)                                                  | 1.12x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 13.4 ms: 1.10x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.49x faster                                          |
| generators               | 76.8 ms                                                | 29.4 ms: 2.62x faster                                         |
| deltablue                | 7.42 ms                                                | 3.79 ms: 1.96x faster                                         |
| asyncio_tcp              | 925 ms                                                 | 509 ms: 1.82x faster                                          |
| richards_super           | 90.7 ms                                                | 51.2 ms: 1.77x faster                                         |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                        |
| richards                 | 74.9 ms                                                | 45.0 ms: 1.66x faster                                         |
| chaos                    | 106 ms                                                 | 64.6 ms: 1.65x faster                                         |
| logging_silent           | 175 ns                                                 | 110 ns: 1.59x faster                                          |
| go                       | 229 ms                                                 | 144 ms: 1.59x faster                                          |
| raytrace                 | 464 ms                                                 | 299 ms: 1.55x faster                                          |
| scimark_sor              | 197 ms                                                 | 128 ms: 1.54x faster                                          |
| unpack_sequence          | 64.7 ns                                                | 43.2 ns: 1.50x faster                                         |
| python_startup           | 14.2 ms                                                | 9.48 ms: 1.49x faster                                         |
| sqlglot_parse            | 2.06 ms                                                | 1.38 ms: 1.49x faster                                         |
| scimark_monte_carlo      | 108 ms                                                 | 72.6 ms: 1.49x faster                                         |
| nbody                    | 142 ms                                                 | 96.3 ms: 1.47x faster                                         |
| async_tree_none          | 717 ms                                                 | 499 ms: 1.44x faster                                          |
| pickle_pure_python       | 455 us                                                 | 317 us: 1.43x faster                                          |
| sqlglot_transpile        | 2.45 ms                                                | 1.71 ms: 1.43x faster                                         |
| async_tree_io            | 1.77 sec                                               | 1.24 sec: 1.43x faster                                        |
| async_tree_memoization   | 854 ms                                                 | 606 ms: 1.41x faster                                          |
| coroutines               | 31.8 ms                                                | 22.7 ms: 1.40x faster                                         |
| pyflate                  | 673 ms                                                 | 480 ms: 1.40x faster                                          |
| hexiom                   | 9.53 ms                                                | 6.82 ms: 1.40x faster                                         |
| json_dumps               | 13.5 ms                                                | 9.76 ms: 1.39x faster                                         |
| logging_format           | 8.91 us                                                | 6.55 us: 1.36x faster                                         |
| unpickle_pure_python     | 300 us                                                 | 221 us: 1.36x faster                                          |
| spectral_norm            | 150 ms                                                 | 111 ms: 1.36x faster                                          |
| logging_simple           | 8.07 us                                                | 5.99 us: 1.35x faster                                         |
| crypto_pyaes             | 118 ms                                                 | 88.5 ms: 1.34x faster                                         |
| pprint_pformat           | 1.99 sec                                               | 1.52 sec: 1.31x faster                                        |
| tornado_http             | 127 ms                                                 | 98.7 ms: 1.29x faster                                         |
| pprint_safe_repr         | 955 ms                                                 | 742 ms: 1.29x faster                                          |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 740 ms: 1.29x faster                                          |
| pycparser                | 1.50 sec                                               | 1.17 sec: 1.28x faster                                        |
| xml_etree_process        | 74.9 ms                                                | 58.8 ms: 1.27x faster                                         |
| sqlglot_normalize        | 135 ms                                                 | 108 ms: 1.25x faster                                          |
| mypy2                    | 428 ms                                                 | 343 ms: 1.25x faster                                          |
| regex_compile            | 177 ms                                                 | 142 ms: 1.24x faster                                          |
| deepcopy                 | 442 us                                                 | 362 us: 1.22x faster                                          |
| float                    | 111 ms                                                 | 91.2 ms: 1.21x faster                                         |
| sqlglot_optimize         | 65.3 ms                                                | 54.1 ms: 1.21x faster                                         |
| deepcopy_reduce          | 3.82 us                                                | 3.19 us: 1.20x faster                                         |
| tomli_loads              | 2.92 sec                                               | 2.47 sec: 1.18x faster                                        |
| docutils                 | 3.17 sec                                               | 2.71 sec: 1.17x faster                                        |
| dulwich_log              | 75.9 ms                                                | 65.5 ms: 1.16x faster                                         |
| json_loads               | 28.8 us                                                | 24.9 us: 1.16x faster                                         |
| nqueens                  | 100 ms                                                 | 86.7 ms: 1.15x faster                                         |
| scimark_lu               | 163 ms                                                 | 142 ms: 1.15x faster                                          |
| scimark_fft              | 424 ms                                                 | 371 ms: 1.14x faster                                          |
| json                     | 5.42 ms                                                | 4.77 ms: 1.14x faster                                         |
| bench_thread_pool        | 947 us                                                 | 839 us: 1.13x faster                                          |
| regex_v8                 | 25.0 ms                                                | 22.3 ms: 1.12x faster                                         |
| create_gc_cycles         | 1.67 ms                                                | 1.49 ms: 1.12x faster                                         |
| regex_dna                | 222 ms                                                 | 201 ms: 1.11x faster                                          |
| mako                     | 14.8 ms                                                | 13.4 ms: 1.10x faster                                         |
| mdp                      | 2.82 sec                                               | 2.57 sec: 1.10x faster                                        |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                          |
| comprehensions           | 26.8 us                                                | 24.7 us: 1.09x faster                                         |
| xml_etree_generate       | 94.2 ms                                                | 86.8 ms: 1.09x faster                                         |
| fannkuch                 | 486 ms                                                 | 448 ms: 1.08x faster                                          |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                          |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.10 ms: 1.07x faster                                         |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.06x faster                                          |
| sqlite_synth             | 2.93 us                                                | 2.77 us: 1.06x faster                                         |
| pathlib                  | 20.0 ms                                                | 18.9 ms: 1.06x faster                                         |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                         |
| unpickle_list            | 4.82 us                                                | 4.86 us: 1.01x slower                                         |
| pidigits                 | 190 ms                                                 | 192 ms: 1.01x slower                                          |
| pickle_list              | 4.56 us                                                | 4.62 us: 1.01x slower                                         |
| deepcopy_memo            | 52.3 us                                                | 53.6 us: 1.02x slower                                         |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                         |
| regex_effbot             | 3.23 ms                                                | 3.41 ms: 1.06x slower                                         |
| async_generators         | 425 ms                                                 | 449 ms: 1.06x slower                                          |
| telco                    | 6.54 ms                                                | 6.98 ms: 1.07x slower                                         |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.08x slower                                         |
| gc_traversal             | 3.84 ms                                                | 4.32 ms: 1.12x slower                                         |
| pickle_dict              | 27.3 us                                                | 31.1 us: 1.14x slower                                         |
| python_startup_no_site   | 5.82 ms                                                | 6.90 ms: 1.19x slower                                         |
| dask                     | 423 ms                                                 | 529 ms: 1.25x slower                                          |
| coverage                 | 72.8 ms                                                | 93.8 ms: 1.29x slower                                         |
| Geometric mean           | (ref)                                                  | 1.25x faster                                                  |
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
