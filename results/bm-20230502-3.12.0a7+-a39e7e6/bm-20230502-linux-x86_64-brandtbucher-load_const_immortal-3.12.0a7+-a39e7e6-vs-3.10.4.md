
# Results vs. 3.10.4

- fork: brandtbucher
- ref: load_const_immortal
- machine: linux-x86_64
- commit hash: a39e7e6
- commit date: 2023-05-02
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 270 ms: 1.24x faster                                                        |
| docutils       | 3.17 sec                                               | 2.71 sec: 1.17x faster                                                      |
| tornado_http   | 127 ms                                                 | 99.8 ms: 1.28x faster                                                       |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.3 ms: 1.57x faster                                                       |
| float          | 111 ms                                                 | 81.6 ms: 1.36x faster                                                       |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 146 ms: 1.21x faster                                                        |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                       |
| regex_dna      | 222 ms                                                 | 200 ms: 1.11x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 317 us: 1.44x faster                                                        |
| unpickle_pure_python | 300 us                                                 | 220 us: 1.37x faster                                                        |
| json_dumps           | 13.5 ms                                                | 10.0 ms: 1.35x faster                                                       |
| xml_etree_process    | 74.9 ms                                                | 59.4 ms: 1.26x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 84.8 ms: 1.11x faster                                                       |
| json_loads           | 28.8 us                                                | 26.2 us: 1.10x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.08x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.62 us: 1.01x slower                                                       |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.02x slower                                                       |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                       |
| unpickle             | 14.1 us                                                | 14.7 us: 1.04x slower                                                       |
| pickle_dict          | 27.3 us                                                | 30.7 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.21 ms: 1.54x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.74 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.36x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 32.8 ms: 2.34x faster                                                       |
| deltablue               | 7.42 ms                                                | 3.54 ms: 2.09x faster                                                       |
| asyncio_tcp             | 925 ms                                                 | 507 ms: 1.82x faster                                                        |
| logging_silent          | 175 ns                                                 | 101 ns: 1.74x faster                                                        |
| richards                | 74.9 ms                                                | 44.6 ms: 1.68x faster                                                       |
| go                      | 229 ms                                                 | 138 ms: 1.66x faster                                                        |
| scimark_sor             | 197 ms                                                 | 124 ms: 1.58x faster                                                        |
| nbody                   | 142 ms                                                 | 90.3 ms: 1.57x faster                                                       |
| chaos                   | 106 ms                                                 | 68.6 ms: 1.55x faster                                                       |
| python_startup          | 14.2 ms                                                | 9.21 ms: 1.54x faster                                                       |
| raytrace                | 464 ms                                                 | 304 ms: 1.52x faster                                                        |
| sqlglot_parse           | 2.06 ms                                                | 1.35 ms: 1.52x faster                                                       |
| hexiom                  | 9.53 ms                                                | 6.27 ms: 1.52x faster                                                       |
| pyflate                 | 673 ms                                                 | 450 ms: 1.50x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 80.6 ms: 1.47x faster                                                       |
| scimark_monte_carlo     | 108 ms                                                 | 73.8 ms: 1.47x faster                                                       |
| sqlglot_transpile       | 2.45 ms                                                | 1.68 ms: 1.46x faster                                                       |
| scimark_lu              | 163 ms                                                 | 113 ms: 1.45x faster                                                        |
| pickle_pure_python      | 455 us                                                 | 317 us: 1.44x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.24 sec: 1.43x faster                                                      |
| async_tree_none         | 717 ms                                                 | 503 ms: 1.42x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 37.6 us: 1.39x faster                                                       |
| async_tree_memoization  | 854 ms                                                 | 615 ms: 1.39x faster                                                        |
| spectral_norm           | 150 ms                                                 | 109 ms: 1.38x faster                                                        |
| coroutines              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                       |
| unpickle_pure_python    | 300 us                                                 | 220 us: 1.37x faster                                                        |
| mako                    | 14.8 ms                                                | 10.8 ms: 1.36x faster                                                       |
| float                   | 111 ms                                                 | 81.6 ms: 1.36x faster                                                       |
| json_dumps              | 13.5 ms                                                | 10.0 ms: 1.35x faster                                                       |
| pprint_pformat          | 1.99 sec                                               | 1.50 sec: 1.32x faster                                                      |
| async_tree_cpu_io_mixed | 951 ms                                                 | 727 ms: 1.31x faster                                                        |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.30x faster                                                      |
| pprint_safe_repr        | 955 ms                                                 | 742 ms: 1.29x faster                                                        |
| tornado_http            | 127 ms                                                 | 99.8 ms: 1.28x faster                                                       |
| logging_simple          | 8.07 us                                                | 6.36 us: 1.27x faster                                                       |
| fannkuch                | 486 ms                                                 | 385 ms: 1.26x faster                                                        |
| xml_etree_process       | 74.9 ms                                                | 59.4 ms: 1.26x faster                                                       |
| logging_format          | 8.91 us                                                | 7.16 us: 1.25x faster                                                       |
| 2to3                    | 336 ms                                                 | 270 ms: 1.24x faster                                                        |
| nqueens                 | 100 ms                                                 | 80.6 ms: 1.24x faster                                                       |
| mypy2                   | 428 ms                                                 | 351 ms: 1.22x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 53.4 ns: 1.21x faster                                                       |
| regex_compile           | 177 ms                                                 | 146 ms: 1.21x faster                                                        |
| deepcopy                | 442 us                                                 | 366 us: 1.21x faster                                                        |
| deepcopy_reduce         | 3.82 us                                                | 3.21 us: 1.19x faster                                                       |
| scimark_fft             | 424 ms                                                 | 356 ms: 1.19x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 114 ms: 1.18x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                | 55.3 ms: 1.18x faster                                                       |
| docutils                | 3.17 sec                                               | 2.71 sec: 1.17x faster                                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.77 ms: 1.14x faster                                                       |
| comprehensions          | 26.8 us                                                | 23.5 us: 1.14x faster                                                       |
| bench_thread_pool       | 947 us                                                 | 838 us: 1.13x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                       |
| sqlalchemy_declarative  | 165 ms                                                 | 147 ms: 1.12x faster                                                        |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.12x faster                                                       |
| dulwich_log             | 75.9 ms                                                | 68.3 ms: 1.11x faster                                                       |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.1 ms: 1.11x faster                                                       |
| xml_etree_generate      | 94.2 ms                                                | 84.8 ms: 1.11x faster                                                       |
| regex_dna               | 222 ms                                                 | 200 ms: 1.11x faster                                                        |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                        |
| json_loads              | 28.8 us                                                | 26.2 us: 1.10x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.58 sec: 1.09x faster                                                      |
| sqlite_synth            | 2.93 us                                                | 2.69 us: 1.09x faster                                                       |
| json                    | 5.42 ms                                                | 5.00 ms: 1.08x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.08x faster                                                        |
| pathlib                 | 20.0 ms                                                | 18.7 ms: 1.07x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 154 ms: 1.06x faster                                                        |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                       |
| gc_traversal            | 3.84 ms                                                | 3.89 ms: 1.01x slower                                                       |
| pickle_list             | 4.56 us                                                | 4.62 us: 1.01x slower                                                       |
| unpickle_list           | 4.82 us                                                | 4.94 us: 1.02x slower                                                       |
| pickle                  | 10.3 us                                                | 10.7 us: 1.04x slower                                                       |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                        |
| unpickle                | 14.1 us                                                | 14.7 us: 1.04x slower                                                       |
| async_generators        | 425 ms                                                 | 451 ms: 1.06x slower                                                        |
| telco                   | 6.54 ms                                                | 6.94 ms: 1.06x slower                                                       |
| regex_effbot            | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                       |
| pickle_dict             | 27.3 us                                                | 30.7 us: 1.13x slower                                                       |
| python_startup_no_site  | 5.82 ms                                                | 6.74 ms: 1.16x slower                                                       |
| dask                    | 423 ms                                                 | 542 ms: 1.28x slower                                                        |
| coverage                | 72.8 ms                                                | 102 ms: 1.40x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.24x faster                                                                |
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x
