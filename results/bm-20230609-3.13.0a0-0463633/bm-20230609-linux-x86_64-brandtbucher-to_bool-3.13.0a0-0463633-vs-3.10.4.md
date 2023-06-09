
# Results vs. 3.10.4

- fork: brandtbucher
- ref: to_bool
- machine: linux-x86_64
- commit hash: 0463633
- commit date: 2023-06-09
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.76 sec: 1.15x faster                                         |
| tornado_http   | 127 ms                                                 | 104 ms: 1.23x faster                                           |
| Geometric mean | (ref)                                                  | 1.19x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 94.2 ms: 1.50x faster                                          |
| float          | 111 ms                                                 | 82.2 ms: 1.34x faster                                          |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                  | 1.25x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 148 ms: 1.19x faster                                           |
| regex_v8       | 25.0 ms                                                | 22.7 ms: 1.10x faster                                          |
| regex_dna      | 222 ms                                                 | 212 ms: 1.05x faster                                           |
| regex_effbot   | 3.23 ms                                                | 3.63 ms: 1.12x slower                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 321 us: 1.42x faster                                           |
| json_dumps           | 13.5 ms                                                | 9.86 ms: 1.37x faster                                          |
| unpickle_pure_python | 300 us                                                 | 226 us: 1.33x faster                                           |
| tomli_loads          | 2.92 sec                                               | 2.31 sec: 1.26x faster                                         |
| xml_etree_process    | 74.9 ms                                                | 59.5 ms: 1.26x faster                                          |
| json_loads           | 28.8 us                                                | 24.9 us: 1.16x faster                                          |
| xml_etree_generate   | 94.2 ms                                                | 85.5 ms: 1.10x faster                                          |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                           |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                           |
| pickle_list          | 4.56 us                                                | 4.63 us: 1.02x slower                                          |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                          |
| unpickle_list        | 4.82 us                                                | 5.00 us: 1.04x slower                                          |
| unpickle             | 14.1 us                                                | 15.1 us: 1.07x slower                                          |
| pickle_dict          | 27.3 us                                                | 31.5 us: 1.16x slower                                          |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.35 ms: 1.51x faster                                          |
| python_startup_no_site | 5.82 ms                                                | 6.80 ms: 1.17x slower                                          |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.39x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 144 us: 3.55x faster                                           |
| generators               | 76.8 ms                                                | 32.6 ms: 2.36x faster                                          |
| deltablue                | 7.42 ms                                                | 3.63 ms: 2.04x faster                                          |
| asyncio_tcp              | 925 ms                                                 | 500 ms: 1.85x faster                                           |
| richards_super           | 90.7 ms                                                | 52.5 ms: 1.73x faster                                          |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                         |
| logging_silent           | 175 ns                                                 | 107 ns: 1.64x faster                                           |
| richards                 | 74.9 ms                                                | 45.7 ms: 1.64x faster                                          |
| go                       | 229 ms                                                 | 141 ms: 1.63x faster                                           |
| chaos                    | 106 ms                                                 | 65.9 ms: 1.61x faster                                          |
| python_startup           | 14.2 ms                                                | 9.35 ms: 1.51x faster                                          |
| raytrace                 | 464 ms                                                 | 307 ms: 1.51x faster                                           |
| crypto_pyaes             | 118 ms                                                 | 78.4 ms: 1.51x faster                                          |
| nbody                    | 142 ms                                                 | 94.2 ms: 1.50x faster                                          |
| hexiom                   | 9.53 ms                                                | 6.35 ms: 1.50x faster                                          |
| sqlglot_parse            | 2.06 ms                                                | 1.38 ms: 1.49x faster                                          |
| async_tree_io            | 1.77 sec                                               | 1.21 sec: 1.46x faster                                         |
| async_tree_none          | 717 ms                                                 | 493 ms: 1.45x faster                                           |
| pyflate                  | 673 ms                                                 | 465 ms: 1.45x faster                                           |
| sqlglot_transpile        | 2.45 ms                                                | 1.71 ms: 1.43x faster                                          |
| async_tree_memoization   | 854 ms                                                 | 599 ms: 1.43x faster                                           |
| scimark_monte_carlo      | 108 ms                                                 | 76.2 ms: 1.42x faster                                          |
| pickle_pure_python       | 455 us                                                 | 321 us: 1.42x faster                                           |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.40x faster                                           |
| scimark_sor              | 197 ms                                                 | 141 ms: 1.40x faster                                           |
| scimark_lu               | 163 ms                                                 | 118 ms: 1.39x faster                                           |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.39x faster                                          |
| json_dumps               | 13.5 ms                                                | 9.86 ms: 1.37x faster                                          |
| deepcopy_memo            | 52.3 us                                                | 38.6 us: 1.36x faster                                          |
| coroutines               | 31.8 ms                                                | 23.6 ms: 1.35x faster                                          |
| float                    | 111 ms                                                 | 82.2 ms: 1.34x faster                                          |
| unpickle_pure_python     | 300 us                                                 | 226 us: 1.33x faster                                           |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 734 ms: 1.30x faster                                           |
| pprint_pformat           | 1.99 sec                                               | 1.53 sec: 1.29x faster                                         |
| comprehensions           | 26.8 us                                                | 20.9 us: 1.28x faster                                          |
| pprint_safe_repr         | 955 ms                                                 | 748 ms: 1.28x faster                                           |
| pycparser                | 1.50 sec                                               | 1.19 sec: 1.26x faster                                         |
| tomli_loads              | 2.92 sec                                               | 2.31 sec: 1.26x faster                                         |
| xml_etree_process        | 74.9 ms                                                | 59.5 ms: 1.26x faster                                          |
| fannkuch                 | 486 ms                                                 | 392 ms: 1.24x faster                                           |
| tornado_http             | 127 ms                                                 | 104 ms: 1.23x faster                                           |
| mypy2                    | 428 ms                                                 | 350 ms: 1.22x faster                                           |
| logging_format           | 8.91 us                                                | 7.28 us: 1.22x faster                                          |
| logging_simple           | 8.07 us                                                | 6.61 us: 1.22x faster                                          |
| deepcopy                 | 442 us                                                 | 363 us: 1.22x faster                                           |
| sqlglot_normalize        | 135 ms                                                 | 112 ms: 1.21x faster                                           |
| unpack_sequence          | 64.7 ns                                                | 53.6 ns: 1.21x faster                                          |
| regex_compile            | 177 ms                                                 | 148 ms: 1.19x faster                                           |
| nqueens                  | 100 ms                                                 | 83.9 ms: 1.19x faster                                          |
| deepcopy_reduce          | 3.82 us                                                | 3.23 us: 1.18x faster                                          |
| sqlglot_optimize         | 65.3 ms                                                | 55.2 ms: 1.18x faster                                          |
| scimark_fft              | 424 ms                                                 | 364 ms: 1.16x faster                                           |
| json_loads               | 28.8 us                                                | 24.9 us: 1.16x faster                                          |
| docutils                 | 3.17 sec                                               | 2.76 sec: 1.15x faster                                         |
| bench_thread_pool        | 947 us                                                 | 834 us: 1.14x faster                                           |
| json                     | 5.42 ms                                                | 4.83 ms: 1.12x faster                                          |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                          |
| dulwich_log              | 75.9 ms                                                | 68.9 ms: 1.10x faster                                          |
| xml_etree_generate       | 94.2 ms                                                | 85.5 ms: 1.10x faster                                          |
| regex_v8                 | 25.0 ms                                                | 22.7 ms: 1.10x faster                                          |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.02 ms: 1.09x faster                                          |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                          |
| meteor_contest           | 115 ms                                                 | 107 ms: 1.07x faster                                           |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                          |
| xml_etree_iterparse      | 111 ms                                                 | 105 ms: 1.06x faster                                           |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                           |
| mdp                      | 2.82 sec                                               | 2.67 sec: 1.06x faster                                         |
| regex_dna                | 222 ms                                                 | 212 ms: 1.05x faster                                           |
| gc_traversal             | 3.84 ms                                                | 3.82 ms: 1.01x faster                                          |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                          |
| pickle_list              | 4.56 us                                                | 4.63 us: 1.02x slower                                          |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                          |
| unpickle_list            | 4.82 us                                                | 5.00 us: 1.04x slower                                          |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                           |
| telco                    | 6.54 ms                                                | 6.92 ms: 1.06x slower                                          |
| unpickle                 | 14.1 us                                                | 15.1 us: 1.07x slower                                          |
| async_generators         | 425 ms                                                 | 455 ms: 1.07x slower                                           |
| regex_effbot             | 3.23 ms                                                | 3.63 ms: 1.12x slower                                          |
| pickle_dict              | 27.3 us                                                | 31.5 us: 1.16x slower                                          |
| python_startup_no_site   | 5.82 ms                                                | 6.80 ms: 1.17x slower                                          |
| dask                     | 423 ms                                                 | 546 ms: 1.29x slower                                           |
| coverage                 | 72.8 ms                                                | 97.5 ms: 1.34x slower                                          |
| Geometric mean           | (ref)                                                  | 1.25x faster                                                   |
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
