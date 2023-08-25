
# Results vs. 3.10.4

- fork: brandtbucher
- ref: binary_subscr_str_in
- machine: linux-x86_64
- commit hash: f077383
- commit date: 2023-08-05
- overall geometric mean: 1.31x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.64 sec: 1.20x faster                                                      |
| tornado_http   | 127 ms                                                 | 95.4 ms: 1.34x faster                                                       |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.3 ms: 1.53x faster                                                       |
| float          | 111 ms                                                 | 79.2 ms: 1.39x faster                                                       |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                       |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.44 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 293 us: 1.56x faster                                                        |
| tomli_loads          | 2.92 sec                                               | 2.08 sec: 1.40x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 214 us: 1.40x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.70 ms: 1.39x faster                                                       |
| xml_etree_process    | 74.9 ms                                                | 58.0 ms: 1.29x faster                                                       |
| json_loads           | 28.8 us                                                | 25.3 us: 1.14x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 84.1 ms: 1.12x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.51 us: 1.01x faster                                                       |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                       |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                                       |
| unpickle             | 14.1 us                                                | 14.8 us: 1.05x slower                                                       |
| pickle_dict          | 27.3 us                                                | 32.1 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.40 ms: 1.51x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.87 ms: 1.18x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.37x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 149 us: 3.42x faster                                                        |
| generators               | 76.8 ms                                                | 28.5 ms: 2.69x faster                                                       |
| deltablue                | 7.42 ms                                                | 3.18 ms: 2.33x faster                                                       |
| asyncio_tcp              | 925 ms                                                 | 484 ms: 1.91x faster                                                        |
| chaos                    | 106 ms                                                 | 59.0 ms: 1.80x faster                                                       |
| raytrace                 | 464 ms                                                 | 267 ms: 1.74x faster                                                        |
| logging_silent           | 175 ns                                                 | 104 ns: 1.69x faster                                                        |
| richards_super           | 90.7 ms                                                | 53.8 ms: 1.69x faster                                                       |
| crypto_pyaes             | 118 ms                                                 | 70.6 ms: 1.68x faster                                                       |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                      |
| go                       | 229 ms                                                 | 139 ms: 1.65x faster                                                        |
| scimark_sor              | 197 ms                                                 | 120 ms: 1.64x faster                                                        |
| sqlglot_parse            | 2.06 ms                                                | 1.26 ms: 1.64x faster                                                       |
| scimark_monte_carlo      | 108 ms                                                 | 66.9 ms: 1.62x faster                                                       |
| hexiom                   | 9.53 ms                                                | 6.03 ms: 1.58x faster                                                       |
| richards                 | 74.9 ms                                                | 47.6 ms: 1.57x faster                                                       |
| pickle_pure_python       | 455 us                                                 | 293 us: 1.56x faster                                                        |
| sqlglot_transpile        | 2.45 ms                                                | 1.58 ms: 1.55x faster                                                       |
| nbody                    | 142 ms                                                 | 92.3 ms: 1.53x faster                                                       |
| pyflate                  | 673 ms                                                 | 443 ms: 1.52x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 1.17 sec: 1.52x faster                                                      |
| python_startup           | 14.2 ms                                                | 9.40 ms: 1.51x faster                                                       |
| async_tree_none          | 717 ms                                                 | 478 ms: 1.50x faster                                                        |
| coroutines               | 31.8 ms                                                | 21.4 ms: 1.48x faster                                                       |
| scimark_lu               | 163 ms                                                 | 110 ms: 1.48x faster                                                        |
| async_tree_memoization   | 854 ms                                                 | 582 ms: 1.47x faster                                                        |
| unpack_sequence          | 64.7 ns                                                | 44.7 ns: 1.45x faster                                                       |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.45x faster                                                        |
| tomli_loads              | 2.92 sec                                               | 2.08 sec: 1.40x faster                                                      |
| unpickle_pure_python     | 300 us                                                 | 214 us: 1.40x faster                                                        |
| json_dumps               | 13.5 ms                                                | 9.70 ms: 1.39x faster                                                       |
| float                    | 111 ms                                                 | 79.2 ms: 1.39x faster                                                       |
| deepcopy_memo            | 52.3 us                                                | 37.7 us: 1.39x faster                                                       |
| logging_format           | 8.91 us                                                | 6.44 us: 1.38x faster                                                       |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.37x faster                                                       |
| pprint_pformat           | 1.99 sec                                               | 1.45 sec: 1.37x faster                                                      |
| logging_simple           | 8.07 us                                                | 5.89 us: 1.37x faster                                                       |
| pprint_safe_repr         | 955 ms                                                 | 710 ms: 1.35x faster                                                        |
| tornado_http             | 127 ms                                                 | 95.4 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 715 ms: 1.33x faster                                                        |
| comprehensions           | 26.8 us                                                | 20.3 us: 1.32x faster                                                       |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.30x faster                                                      |
| sqlglot_normalize        | 135 ms                                                 | 104 ms: 1.30x faster                                                        |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                                        |
| xml_etree_process        | 74.9 ms                                                | 58.0 ms: 1.29x faster                                                       |
| mypy2                    | 428 ms                                                 | 336 ms: 1.27x faster                                                        |
| fannkuch                 | 486 ms                                                 | 386 ms: 1.26x faster                                                        |
| deepcopy                 | 442 us                                                 | 353 us: 1.25x faster                                                        |
| sqlglot_optimize         | 65.3 ms                                                | 52.7 ms: 1.24x faster                                                       |
| nqueens                  | 100 ms                                                 | 82.2 ms: 1.22x faster                                                       |
| deepcopy_reduce          | 3.82 us                                                | 3.16 us: 1.21x faster                                                       |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.51 ms: 1.21x faster                                                       |
| docutils                 | 3.17 sec                                               | 2.64 sec: 1.20x faster                                                      |
| scimark_fft              | 424 ms                                                 | 358 ms: 1.18x faster                                                        |
| dulwich_log              | 75.9 ms                                                | 65.9 ms: 1.15x faster                                                       |
| bench_thread_pool        | 947 us                                                 | 824 us: 1.15x faster                                                        |
| regex_v8                 | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                       |
| json_loads               | 28.8 us                                                | 25.3 us: 1.14x faster                                                       |
| json                     | 5.42 ms                                                | 4.76 ms: 1.14x faster                                                       |
| create_gc_cycles         | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                       |
| xml_etree_generate       | 94.2 ms                                                | 84.1 ms: 1.12x faster                                                       |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                                        |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                        |
| pathlib                  | 20.0 ms                                                | 18.6 ms: 1.08x faster                                                       |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                                       |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                                        |
| mdp                      | 2.82 sec                                               | 2.64 sec: 1.07x faster                                                      |
| regex_dna                | 222 ms                                                 | 207 ms: 1.07x faster                                                        |
| gc_traversal             | 3.84 ms                                                | 3.67 ms: 1.05x faster                                                       |
| pickle_list              | 4.56 us                                                | 4.51 us: 1.01x faster                                                       |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                       |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                                       |
| unpickle_list            | 4.82 us                                                | 4.99 us: 1.04x slower                                                       |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.05x slower                                                       |
| async_generators         | 425 ms                                                 | 449 ms: 1.06x slower                                                        |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                                        |
| regex_effbot             | 3.23 ms                                                | 3.44 ms: 1.06x slower                                                       |
| pickle_dict              | 27.3 us                                                | 32.1 us: 1.18x slower                                                       |
| python_startup_no_site   | 5.82 ms                                                | 6.87 ms: 1.18x slower                                                       |
| telco                    | 6.54 ms                                                | 7.76 ms: 1.19x slower                                                       |
| dask                     | 423 ms                                                 | 518 ms: 1.23x slower                                                        |
| coverage                 | 72.8 ms                                                | 94.2 ms: 1.29x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.31x faster                                                                |
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.23x
