
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_binary_subscr
- machine: linux-x86_64
- commit hash: b174015
- commit date: 2023-03-23
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 254 ms: 1.32x faster                                                         |
| chameleon      | 9.13 ms                                                             | 6.52 ms: 1.40x faster                                                        |
| docutils       | 3.19 sec                                                            | 2.56 sec: 1.25x faster                                                       |
| html5lib       | 86.4 ms                                                             | 62.2 ms: 1.39x faster                                                        |
| tornado_http   | 129 ms                                                              | 91.4 ms: 1.41x faster                                                        |
| Geometric mean | (ref)                                                               | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 88.5 ms: 1.65x faster                                                        |
| float          | 110 ms                                                              | 74.0 ms: 1.48x faster                                                        |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                               | 1.35x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 134 ms: 1.33x faster                                                         |
| regex_v8       | 24.9 ms                                                             | 22.2 ms: 1.12x faster                                                        |
| regex_dna      | 213 ms                                                              | 211 ms: 1.01x faster                                                         |
| regex_effbot   | 3.22 ms                                                             | 3.53 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                               | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 287 us: 1.59x faster                                                         |
| unpickle_pure_python | 300 us                                                              | 202 us: 1.49x faster                                                         |
| json_dumps           | 13.7 ms                                                             | 9.68 ms: 1.42x faster                                                        |
| xml_etree_process    | 74.8 ms                                                             | 57.2 ms: 1.31x faster                                                        |
| json_loads           | 29.3 us                                                             | 23.9 us: 1.23x faster                                                        |
| xml_etree_generate   | 94.9 ms                                                             | 82.1 ms: 1.16x faster                                                        |
| unpickle             | 15.0 us                                                             | 13.3 us: 1.13x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                              | 100.0 ms: 1.11x faster                                                       |
| xml_etree_parse      | 164 ms                                                              | 148 ms: 1.10x faster                                                         |
| pickle_list          | 4.73 us                                                             | 4.37 us: 1.08x faster                                                        |
| pickle               | 10.2 us                                                             | 10.4 us: 1.02x slower                                                        |
| unpickle_list        | 4.94 us                                                             | 5.03 us: 1.02x slower                                                        |
| pickle_dict          | 27.8 us                                                             | 31.1 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                               | 1.17x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.84 ms: 1.60x faster                                                        |
| python_startup_no_site | 5.80 ms                                                             | 6.53 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                               | 1.19x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.85 ms: 1.50x faster                                                        |
| genshi_text     | 30.4 ms                                                             | 21.5 ms: 1.42x faster                                                        |
| django_template | 45.8 ms                                                             | 33.0 ms: 1.39x faster                                                        |
| genshi_xml      | 64.3 ms                                                             | 47.7 ms: 1.35x faster                                                        |
| Geometric mean  | (ref)                                                               | 1.41x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.1 ms: 2.60x faster                                                        |
| deltablue               | 7.30 ms                                                             | 3.19 ms: 2.29x faster                                                        |
| asyncio_tcp             | 922 ms                                                              | 507 ms: 1.82x faster                                                         |
| scimark_sor             | 198 ms                                                              | 111 ms: 1.79x faster                                                         |
| richards                | 74.2 ms                                                             | 42.9 ms: 1.73x faster                                                        |
| logging_silent          | 169 ns                                                              | 97.9 ns: 1.73x faster                                                        |
| raytrace                | 470 ms                                                              | 278 ms: 1.69x faster                                                         |
| nbody                   | 146 ms                                                              | 88.5 ms: 1.65x faster                                                        |
| pyflate                 | 671 ms                                                              | 416 ms: 1.61x faster                                                         |
| go                      | 226 ms                                                              | 140 ms: 1.61x faster                                                         |
| python_startup          | 14.1 ms                                                             | 8.84 ms: 1.60x faster                                                        |
| pickle_pure_python      | 457 us                                                              | 287 us: 1.59x faster                                                         |
| spectral_norm           | 150 ms                                                              | 94.5 ms: 1.59x faster                                                        |
| crypto_pyaes            | 117 ms                                                              | 73.5 ms: 1.59x faster                                                        |
| chaos                   | 106 ms                                                              | 66.9 ms: 1.58x faster                                                        |
| hexiom                  | 9.50 ms                                                             | 6.03 ms: 1.58x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                              | 69.1 ms: 1.57x faster                                                        |
| unpack_sequence         | 65.6 ns                                                             | 42.4 ns: 1.55x faster                                                        |
| deepcopy_memo           | 51.8 us                                                             | 34.2 us: 1.52x faster                                                        |
| scimark_lu              | 160 ms                                                              | 107 ms: 1.50x faster                                                         |
| mako                    | 14.7 ms                                                             | 9.85 ms: 1.50x faster                                                        |
| unpickle_pure_python    | 300 us                                                              | 202 us: 1.49x faster                                                         |
| float                   | 110 ms                                                              | 74.0 ms: 1.48x faster                                                        |
| sqlglot_parse           | 2.07 ms                                                             | 1.43 ms: 1.44x faster                                                        |
| logging_format          | 9.07 us                                                             | 6.38 us: 1.42x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                             | 1.73 ms: 1.42x faster                                                        |
| logging_simple          | 8.21 us                                                             | 5.78 us: 1.42x faster                                                        |
| genshi_text             | 30.4 ms                                                             | 21.5 ms: 1.42x faster                                                        |
| json_dumps              | 13.7 ms                                                             | 9.68 ms: 1.42x faster                                                        |
| tornado_http            | 129 ms                                                              | 91.4 ms: 1.41x faster                                                        |
| chameleon               | 9.13 ms                                                             | 6.52 ms: 1.40x faster                                                        |
| scimark_fft             | 425 ms                                                              | 306 ms: 1.39x faster                                                         |
| pprint_safe_repr        | 953 ms                                                              | 685 ms: 1.39x faster                                                         |
| pprint_pformat          | 1.98 sec                                                            | 1.42 sec: 1.39x faster                                                       |
| django_template         | 45.8 ms                                                             | 33.0 ms: 1.39x faster                                                        |
| html5lib                | 86.4 ms                                                             | 62.2 ms: 1.39x faster                                                        |
| coroutines              | 31.8 ms                                                             | 23.0 ms: 1.38x faster                                                        |
| async_tree_io           | 1.78 sec                                                            | 1.30 sec: 1.37x faster                                                       |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.14 ms: 1.36x faster                                                        |
| async_tree_none         | 713 ms                                                              | 526 ms: 1.35x faster                                                         |
| genshi_xml              | 64.3 ms                                                             | 47.7 ms: 1.35x faster                                                        |
| deepcopy                | 438 us                                                              | 326 us: 1.34x faster                                                         |
| aiohttp                 | 1.35 ms                                                             | 1.02 ms: 1.33x faster                                                        |
| regex_compile           | 177 ms                                                              | 134 ms: 1.33x faster                                                         |
| 2to3                    | 336 ms                                                              | 254 ms: 1.32x faster                                                         |
| pycparser               | 1.53 sec                                                            | 1.16 sec: 1.32x faster                                                       |
| gunicorn                | 1.43 ms                                                             | 1.09 ms: 1.31x faster                                                        |
| xml_etree_process       | 74.8 ms                                                             | 57.2 ms: 1.31x faster                                                        |
| async_tree_memoization  | 853 ms                                                              | 656 ms: 1.30x faster                                                         |
| mypy2                   | 432 ms                                                              | 333 ms: 1.29x faster                                                         |
| sqlglot_normalize       | 135 ms                                                              | 104 ms: 1.29x faster                                                         |
| deepcopy_reduce         | 3.80 us                                                             | 2.95 us: 1.29x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                             | 50.8 ms: 1.28x faster                                                        |
| thrift                  | 1.04 ms                                                             | 812 us: 1.28x faster                                                         |
| async_tree_cpu_io_mixed | 944 ms                                                              | 746 ms: 1.27x faster                                                         |
| fannkuch                | 485 ms                                                              | 383 ms: 1.27x faster                                                         |
| docutils                | 3.19 sec                                                            | 2.56 sec: 1.25x faster                                                       |
| json_loads              | 29.3 us                                                             | 23.9 us: 1.23x faster                                                        |
| bench_thread_pool       | 954 us                                                              | 790 us: 1.21x faster                                                         |
| sqlalchemy_declarative  | 166 ms                                                              | 138 ms: 1.20x faster                                                         |
| dulwich_log             | 76.3 ms                                                             | 63.6 ms: 1.20x faster                                                        |
| nqueens                 | 98.8 ms                                                             | 82.6 ms: 1.20x faster                                                        |
| json                    | 5.41 ms                                                             | 4.55 ms: 1.19x faster                                                        |
| sympy_integrate         | 24.3 ms                                                             | 20.5 ms: 1.19x faster                                                        |
| sqlalchemy_imperative   | 21.2 ms                                                             | 18.0 ms: 1.17x faster                                                        |
| sympy_expand            | 540 ms                                                              | 462 ms: 1.17x faster                                                         |
| xml_etree_generate      | 94.9 ms                                                             | 82.1 ms: 1.16x faster                                                        |
| sympy_str               | 328 ms                                                              | 284 ms: 1.15x faster                                                         |
| comprehensions          | 27.3 us                                                             | 23.7 us: 1.15x faster                                                        |
| sqlite_synth            | 2.97 us                                                             | 2.62 us: 1.14x faster                                                        |
| unpickle                | 15.0 us                                                             | 13.3 us: 1.13x faster                                                        |
| regex_v8                | 24.9 ms                                                             | 22.2 ms: 1.12x faster                                                        |
| meteor_contest          | 115 ms                                                              | 102 ms: 1.12x faster                                                         |
| djangocms               | 36.3 us                                                             | 32.6 us: 1.12x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                              | 100.0 ms: 1.11x faster                                                       |
| sympy_sum               | 185 ms                                                              | 167 ms: 1.11x faster                                                         |
| create_gc_cycles        | 1.64 ms                                                             | 1.49 ms: 1.10x faster                                                        |
| xml_etree_parse         | 164 ms                                                              | 148 ms: 1.10x faster                                                         |
| pathlib                 | 19.8 ms                                                             | 18.2 ms: 1.09x faster                                                        |
| pickle_list             | 4.73 us                                                             | 4.37 us: 1.08x faster                                                        |
| telco                   | 6.67 ms                                                             | 6.49 ms: 1.03x faster                                                        |
| async_generators        | 420 ms                                                              | 409 ms: 1.03x faster                                                         |
| mdp                     | 2.75 sec                                                            | 2.68 sec: 1.03x faster                                                       |
| regex_dna               | 213 ms                                                              | 211 ms: 1.01x faster                                                         |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                         |
| bench_mp_pool           | 24.0 ms                                                             | 24.0 ms: 1.00x slower                                                        |
| pickle                  | 10.2 us                                                             | 10.4 us: 1.02x slower                                                        |
| unpickle_list           | 4.94 us                                                             | 5.03 us: 1.02x slower                                                        |
| regex_effbot            | 3.22 ms                                                             | 3.53 ms: 1.09x slower                                                        |
| gc_traversal            | 3.53 ms                                                             | 3.90 ms: 1.11x slower                                                        |
| pickle_dict             | 27.8 us                                                             | 31.1 us: 1.12x slower                                                        |
| python_startup_no_site  | 5.80 ms                                                             | 6.53 ms: 1.13x slower                                                        |
| dask                    | 437 ms                                                              | 512 ms: 1.17x slower                                                         |
| coverage                | 70.6 ms                                                             | 96.1 ms: 1.36x slower                                                        |
| Geometric mean          | (ref)                                                               | 1.29x faster                                                                 |
<<<<<<< HEAD
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
=======
Ignored benchmarks (2) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
>>>>>>> a4b1e308 (BUGFIX: match to the the base commit from the same machine)
