
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_call
- machine: linux-x86_64
- commit hash: 187f060
- commit date: 2023-03-25
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 251 ms: 1.34x faster                                                |
| chameleon      | 9.13 ms                                                             | 6.48 ms: 1.41x faster                                               |
| docutils       | 3.19 sec                                                            | 2.56 sec: 1.25x faster                                              |
| html5lib       | 86.4 ms                                                             | 61.2 ms: 1.41x faster                                               |
| tornado_http   | 129 ms                                                              | 91.6 ms: 1.41x faster                                               |
| Geometric mean | (ref)                                                               | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 88.2 ms: 1.65x faster                                               |
| float          | 110 ms                                                              | 74.4 ms: 1.48x faster                                               |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                               | 1.35x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 135 ms: 1.31x faster                                                |
| regex_v8       | 24.9 ms                                                             | 21.8 ms: 1.14x faster                                               |
| regex_dna      | 213 ms                                                              | 204 ms: 1.04x faster                                                |
| regex_effbot   | 3.22 ms                                                             | 3.64 ms: 1.13x slower                                               |
| Geometric mean | (ref)                                                               | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 289 us: 1.58x faster                                                |
| unpickle_pure_python | 300 us                                                              | 202 us: 1.48x faster                                                |
| json_dumps           | 13.7 ms                                                             | 9.62 ms: 1.42x faster                                               |
| xml_etree_process    | 74.8 ms                                                             | 55.3 ms: 1.35x faster                                               |
| json_loads           | 29.3 us                                                             | 24.3 us: 1.21x faster                                               |
| xml_etree_generate   | 94.9 ms                                                             | 80.2 ms: 1.18x faster                                               |
| pickle_list          | 4.73 us                                                             | 4.21 us: 1.12x faster                                               |
| xml_etree_parse      | 164 ms                                                              | 149 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 111 ms                                                              | 103 ms: 1.08x faster                                                |
| unpickle             | 15.0 us                                                             | 13.9 us: 1.08x faster                                               |
| pickle               | 10.2 us                                                             | 10.3 us: 1.01x slower                                               |
| unpickle_list        | 4.94 us                                                             | 5.17 us: 1.05x slower                                               |
| pickle_dict          | 27.8 us                                                             | 31.5 us: 1.14x slower                                               |
| Geometric mean       | (ref)                                                               | 1.17x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.83 ms: 1.60x faster                                               |
| python_startup_no_site | 5.80 ms                                                             | 6.53 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                               | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.0 ms: 1.47x faster                                               |
| genshi_text     | 30.4 ms                                                             | 21.7 ms: 1.40x faster                                               |
| django_template | 45.8 ms                                                             | 32.8 ms: 1.40x faster                                               |
| genshi_xml      | 64.3 ms                                                             | 48.6 ms: 1.32x faster                                               |
| Geometric mean  | (ref)                                                               | 1.40x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|-------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 28.7 ms: 2.64x faster                                               |
| deltablue               | 7.30 ms                                                             | 3.23 ms: 2.26x faster                                               |
| asyncio_tcp             | 922 ms                                                              | 505 ms: 1.83x faster                                                |
| logging_silent          | 169 ns                                                              | 94.8 ns: 1.78x faster                                               |
| scimark_sor             | 198 ms                                                              | 111 ms: 1.78x faster                                                |
| richards                | 74.2 ms                                                             | 43.4 ms: 1.71x faster                                               |
| raytrace                | 470 ms                                                              | 278 ms: 1.69x faster                                                |
| nbody                   | 146 ms                                                              | 88.2 ms: 1.65x faster                                               |
| go                      | 226 ms                                                              | 139 ms: 1.62x faster                                                |
| scimark_monte_carlo     | 109 ms                                                              | 67.5 ms: 1.61x faster                                               |
| chaos                   | 106 ms                                                              | 66.0 ms: 1.60x faster                                               |
| python_startup          | 14.1 ms                                                             | 8.83 ms: 1.60x faster                                               |
| pyflate                 | 671 ms                                                              | 420 ms: 1.60x faster                                                |
| crypto_pyaes            | 117 ms                                                              | 73.3 ms: 1.59x faster                                               |
| spectral_norm           | 150 ms                                                              | 94.7 ms: 1.58x faster                                               |
| pickle_pure_python      | 457 us                                                              | 289 us: 1.58x faster                                                |
| hexiom                  | 9.50 ms                                                             | 6.05 ms: 1.57x faster                                               |
| deepcopy_memo           | 51.8 us                                                             | 34.1 us: 1.52x faster                                               |
| unpack_sequence         | 65.6 ns                                                             | 44.0 ns: 1.49x faster                                               |
| scimark_lu              | 160 ms                                                              | 108 ms: 1.48x faster                                                |
| unpickle_pure_python    | 300 us                                                              | 202 us: 1.48x faster                                                |
| float                   | 110 ms                                                              | 74.4 ms: 1.48x faster                                               |
| mako                    | 14.7 ms                                                             | 10.0 ms: 1.47x faster                                               |
| logging_format          | 9.07 us                                                             | 6.23 us: 1.45x faster                                               |
| logging_simple          | 8.21 us                                                             | 5.68 us: 1.45x faster                                               |
| sqlglot_parse           | 2.07 ms                                                             | 1.44 ms: 1.43x faster                                               |
| json_dumps              | 13.7 ms                                                             | 9.62 ms: 1.42x faster                                               |
| html5lib                | 86.4 ms                                                             | 61.2 ms: 1.41x faster                                               |
| sqlglot_transpile       | 2.45 ms                                                             | 1.74 ms: 1.41x faster                                               |
| chameleon               | 9.13 ms                                                             | 6.48 ms: 1.41x faster                                               |
| tornado_http            | 129 ms                                                              | 91.6 ms: 1.41x faster                                               |
| genshi_text             | 30.4 ms                                                             | 21.7 ms: 1.40x faster                                               |
| scimark_fft             | 425 ms                                                              | 304 ms: 1.40x faster                                                |
| coroutines              | 31.8 ms                                                             | 22.7 ms: 1.40x faster                                               |
| django_template         | 45.8 ms                                                             | 32.8 ms: 1.40x faster                                               |
| pprint_pformat          | 1.98 sec                                                            | 1.43 sec: 1.39x faster                                              |
| pycparser               | 1.53 sec                                                            | 1.11 sec: 1.38x faster                                              |
| async_tree_io           | 1.78 sec                                                            | 1.29 sec: 1.38x faster                                              |
| pprint_safe_repr        | 953 ms                                                              | 696 ms: 1.37x faster                                                |
| async_tree_none         | 713 ms                                                              | 524 ms: 1.36x faster                                                |
| xml_etree_process       | 74.8 ms                                                             | 55.3 ms: 1.35x faster                                               |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.34x faster                                               |
| 2to3                    | 336 ms                                                              | 251 ms: 1.34x faster                                                |
| thrift                  | 1.04 ms                                                             | 780 us: 1.33x faster                                                |
| deepcopy                | 438 us                                                              | 331 us: 1.32x faster                                                |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.24 ms: 1.32x faster                                               |
| genshi_xml              | 64.3 ms                                                             | 48.6 ms: 1.32x faster                                               |
| regex_compile           | 177 ms                                                              | 135 ms: 1.31x faster                                                |
| gunicorn                | 1.43 ms                                                             | 1.09 ms: 1.31x faster                                               |
| async_tree_memoization  | 853 ms                                                              | 652 ms: 1.31x faster                                                |
| deepcopy_reduce         | 3.80 us                                                             | 2.91 us: 1.31x faster                                               |
| fannkuch                | 485 ms                                                              | 371 ms: 1.31x faster                                                |
| mypy2                   | 432 ms                                                              | 332 ms: 1.30x faster                                                |
| sqlglot_normalize       | 135 ms                                                              | 105 ms: 1.28x faster                                                |
| async_tree_cpu_io_mixed | 944 ms                                                              | 742 ms: 1.27x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                             | 51.4 ms: 1.27x faster                                               |
| docutils                | 3.19 sec                                                            | 2.56 sec: 1.25x faster                                              |
| sqlalchemy_declarative  | 166 ms                                                              | 136 ms: 1.22x faster                                                |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.5 ms: 1.21x faster                                               |
| bench_thread_pool       | 954 us                                                              | 791 us: 1.21x faster                                                |
| json_loads              | 29.3 us                                                             | 24.3 us: 1.21x faster                                               |
| nqueens                 | 98.8 ms                                                             | 82.3 ms: 1.20x faster                                               |
| dulwich_log             | 76.3 ms                                                             | 63.6 ms: 1.20x faster                                               |
| sympy_integrate         | 24.3 ms                                                             | 20.5 ms: 1.19x faster                                               |
| xml_etree_generate      | 94.9 ms                                                             | 80.2 ms: 1.18x faster                                               |
| sympy_expand            | 540 ms                                                              | 461 ms: 1.17x faster                                                |
| sympy_str               | 328 ms                                                              | 282 ms: 1.16x faster                                                |
| json                    | 5.41 ms                                                             | 4.67 ms: 1.16x faster                                               |
| comprehensions          | 27.3 us                                                             | 23.6 us: 1.15x faster                                               |
| regex_v8                | 24.9 ms                                                             | 21.8 ms: 1.14x faster                                               |
| djangocms               | 36.3 us                                                             | 32.1 us: 1.13x faster                                               |
| sqlite_synth            | 2.97 us                                                             | 2.63 us: 1.13x faster                                               |
| pickle_list             | 4.73 us                                                             | 4.21 us: 1.12x faster                                               |
| pathlib                 | 19.8 ms                                                             | 17.7 ms: 1.12x faster                                               |
| sympy_sum               | 185 ms                                                              | 166 ms: 1.11x faster                                                |
| create_gc_cycles        | 1.64 ms                                                             | 1.48 ms: 1.11x faster                                               |
| meteor_contest          | 115 ms                                                              | 104 ms: 1.10x faster                                                |
| xml_etree_parse         | 164 ms                                                              | 149 ms: 1.10x faster                                                |
| xml_etree_iterparse     | 111 ms                                                              | 103 ms: 1.08x faster                                                |
| unpickle                | 15.0 us                                                             | 13.9 us: 1.08x faster                                               |
| regex_dna               | 213 ms                                                              | 204 ms: 1.04x faster                                                |
| mdp                     | 2.75 sec                                                            | 2.68 sec: 1.03x faster                                              |
| async_generators        | 420 ms                                                              | 410 ms: 1.02x faster                                                |
| telco                   | 6.67 ms                                                             | 6.54 ms: 1.02x faster                                               |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                |
| bench_mp_pool           | 24.0 ms                                                             | 24.0 ms: 1.00x slower                                               |
| gc_traversal            | 3.53 ms                                                             | 3.54 ms: 1.00x slower                                               |
| pickle                  | 10.2 us                                                             | 10.3 us: 1.01x slower                                               |
| unpickle_list           | 4.94 us                                                             | 5.17 us: 1.05x slower                                               |
| python_startup_no_site  | 5.80 ms                                                             | 6.53 ms: 1.13x slower                                               |
| regex_effbot            | 3.22 ms                                                             | 3.64 ms: 1.13x slower                                               |
| pickle_dict             | 27.8 us                                                             | 31.5 us: 1.14x slower                                               |
| dask                    | 437 ms                                                              | 511 ms: 1.17x slower                                                |
| coverage                | 70.6 ms                                                             | 96.1 ms: 1.36x slower                                               |
| Geometric mean          | (ref)                                                               | 1.30x faster                                                        |
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
