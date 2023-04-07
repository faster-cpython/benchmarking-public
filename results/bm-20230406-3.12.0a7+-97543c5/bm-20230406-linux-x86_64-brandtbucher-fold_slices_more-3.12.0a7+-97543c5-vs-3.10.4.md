
# Results vs. 3.10.4

- fork: brandtbucher
- ref: fold_slices_more
- machine: linux-x86_64
- commit hash: 97543c5
- commit date: 2023-04-06
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 250 ms: 1.34x faster                                                     |
| chameleon      | 9.13 ms                                                             | 6.41 ms: 1.42x faster                                                    |
| docutils       | 3.19 sec                                                            | 2.53 sec: 1.26x faster                                                   |
| html5lib       | 86.4 ms                                                             | 61.0 ms: 1.42x faster                                                    |
| tornado_http   | 129 ms                                                              | 90.6 ms: 1.42x faster                                                    |
| Geometric mean | (ref)                                                               | 1.37x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 86.9 ms: 1.68x faster                                                    |
| float          | 110 ms                                                              | 74.7 ms: 1.47x faster                                                    |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                               | 1.35x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 132 ms: 1.34x faster                                                     |
| regex_v8       | 24.9 ms                                                             | 21.6 ms: 1.15x faster                                                    |
| regex_dna      | 213 ms                                                              | 204 ms: 1.04x faster                                                     |
| regex_effbot   | 3.22 ms                                                             | 3.41 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                               | 1.11x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 287 us: 1.59x faster                                                     |
| unpickle_pure_python | 300 us                                                              | 202 us: 1.48x faster                                                     |
| json_dumps           | 13.7 ms                                                             | 9.37 ms: 1.46x faster                                                    |
| xml_etree_process    | 74.8 ms                                                             | 55.3 ms: 1.35x faster                                                    |
| json_loads           | 29.3 us                                                             | 24.2 us: 1.21x faster                                                    |
| xml_etree_generate   | 94.9 ms                                                             | 80.6 ms: 1.18x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                              | 99.4 ms: 1.12x faster                                                    |
| xml_etree_parse      | 164 ms                                                              | 147 ms: 1.11x faster                                                     |
| unpickle             | 15.0 us                                                             | 13.8 us: 1.08x faster                                                    |
| pickle_list          | 4.73 us                                                             | 4.43 us: 1.07x faster                                                    |
| unpickle_list        | 4.94 us                                                             | 5.05 us: 1.02x slower                                                    |
| pickle               | 10.2 us                                                             | 10.6 us: 1.04x slower                                                    |
| pickle_dict          | 27.8 us                                                             | 31.9 us: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                               | 1.17x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.82 ms: 1.60x faster                                                    |
| python_startup_no_site | 5.80 ms                                                             | 6.52 ms: 1.13x slower                                                    |
| Geometric mean         | (ref)                                                               | 1.19x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.1 ms: 1.46x faster                                                    |
| genshi_text     | 30.4 ms                                                             | 21.1 ms: 1.44x faster                                                    |
| django_template | 45.8 ms                                                             | 32.4 ms: 1.41x faster                                                    |
| genshi_xml      | 64.3 ms                                                             | 46.9 ms: 1.37x faster                                                    |
| Geometric mean  | (ref)                                                               | 1.42x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.9 ms: 2.53x faster                                                    |
| deltablue               | 7.30 ms                                                             | 3.24 ms: 2.25x faster                                                    |
| asyncio_tcp             | 922 ms                                                              | 500 ms: 1.84x faster                                                     |
| richards                | 74.2 ms                                                             | 41.4 ms: 1.79x faster                                                    |
| logging_silent          | 169 ns                                                              | 95.0 ns: 1.78x faster                                                    |
| scimark_sor             | 198 ms                                                              | 113 ms: 1.75x faster                                                     |
| sqlglot_parse           | 2.07 ms                                                             | 1.22 ms: 1.69x faster                                                    |
| nbody                   | 146 ms                                                              | 86.9 ms: 1.68x faster                                                    |
| raytrace                | 470 ms                                                              | 283 ms: 1.66x faster                                                     |
| sqlglot_transpile       | 2.45 ms                                                             | 1.50 ms: 1.64x faster                                                    |
| go                      | 226 ms                                                              | 138 ms: 1.64x faster                                                     |
| chaos                   | 106 ms                                                              | 65.4 ms: 1.62x faster                                                    |
| hexiom                  | 9.50 ms                                                             | 5.92 ms: 1.61x faster                                                    |
| python_startup          | 14.1 ms                                                             | 8.82 ms: 1.60x faster                                                    |
| pickle_pure_python      | 457 us                                                              | 287 us: 1.59x faster                                                     |
| scimark_monte_carlo     | 109 ms                                                              | 68.2 ms: 1.59x faster                                                    |
| spectral_norm           | 150 ms                                                              | 95.1 ms: 1.58x faster                                                    |
| crypto_pyaes            | 117 ms                                                              | 73.9 ms: 1.58x faster                                                    |
| pyflate                 | 671 ms                                                              | 425 ms: 1.58x faster                                                     |
| deepcopy_memo           | 51.8 us                                                             | 34.3 us: 1.51x faster                                                    |
| unpack_sequence         | 65.6 ns                                                             | 43.5 ns: 1.51x faster                                                    |
| unpickle_pure_python    | 300 us                                                              | 202 us: 1.48x faster                                                     |
| float                   | 110 ms                                                              | 74.7 ms: 1.47x faster                                                    |
| scimark_lu              | 160 ms                                                              | 109 ms: 1.47x faster                                                     |
| mako                    | 14.7 ms                                                             | 10.1 ms: 1.46x faster                                                    |
| json_dumps              | 13.7 ms                                                             | 9.37 ms: 1.46x faster                                                    |
| genshi_text             | 30.4 ms                                                             | 21.1 ms: 1.44x faster                                                    |
| logging_format          | 9.07 us                                                             | 6.30 us: 1.44x faster                                                    |
| logging_simple          | 8.21 us                                                             | 5.71 us: 1.44x faster                                                    |
| chameleon               | 9.13 ms                                                             | 6.41 ms: 1.42x faster                                                    |
| tornado_http            | 129 ms                                                              | 90.6 ms: 1.42x faster                                                    |
| html5lib                | 86.4 ms                                                             | 61.0 ms: 1.42x faster                                                    |
| django_template         | 45.8 ms                                                             | 32.4 ms: 1.41x faster                                                    |
| pprint_pformat          | 1.98 sec                                                            | 1.42 sec: 1.40x faster                                                   |
| async_tree_io           | 1.78 sec                                                            | 1.29 sec: 1.38x faster                                                   |
| pprint_safe_repr        | 953 ms                                                              | 694 ms: 1.37x faster                                                     |
| genshi_xml              | 64.3 ms                                                             | 46.9 ms: 1.37x faster                                                    |
| async_tree_memoization  | 853 ms                                                              | 623 ms: 1.37x faster                                                     |
| async_tree_none         | 713 ms                                                              | 522 ms: 1.37x faster                                                     |
| scimark_fft             | 425 ms                                                              | 314 ms: 1.36x faster                                                     |
| xml_etree_process       | 74.8 ms                                                             | 55.3 ms: 1.35x faster                                                    |
| regex_compile           | 177 ms                                                              | 132 ms: 1.34x faster                                                     |
| deepcopy                | 438 us                                                              | 326 us: 1.34x faster                                                     |
| 2to3                    | 336 ms                                                              | 250 ms: 1.34x faster                                                     |
| coroutines              | 31.8 ms                                                             | 23.7 ms: 1.34x faster                                                    |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.34x faster                                                    |
| pycparser               | 1.53 sec                                                            | 1.15 sec: 1.34x faster                                                   |
| thrift                  | 1.04 ms                                                             | 782 us: 1.33x faster                                                     |
| gunicorn                | 1.43 ms                                                             | 1.09 ms: 1.32x faster                                                    |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.27 ms: 1.32x faster                                                    |
| deepcopy_reduce         | 3.80 us                                                             | 2.92 us: 1.30x faster                                                    |
| sqlglot_normalize       | 135 ms                                                              | 104 ms: 1.30x faster                                                     |
| sqlglot_optimize        | 65.3 ms                                                             | 50.4 ms: 1.30x faster                                                    |
| mypy2                   | 432 ms                                                              | 334 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed | 944 ms                                                              | 733 ms: 1.29x faster                                                     |
| fannkuch                | 485 ms                                                              | 383 ms: 1.27x faster                                                     |
| docutils                | 3.19 sec                                                            | 2.53 sec: 1.26x faster                                                   |
| comprehensions          | 27.3 us                                                             | 21.9 us: 1.24x faster                                                    |
| sqlalchemy_declarative  | 166 ms                                                              | 136 ms: 1.23x faster                                                     |
| json_loads              | 29.3 us                                                             | 24.2 us: 1.21x faster                                                    |
| dulwich_log             | 76.3 ms                                                             | 63.1 ms: 1.21x faster                                                    |
| bench_thread_pool       | 954 us                                                              | 791 us: 1.21x faster                                                     |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.6 ms: 1.20x faster                                                    |
| nqueens                 | 98.8 ms                                                             | 82.6 ms: 1.20x faster                                                    |
| sympy_integrate         | 24.3 ms                                                             | 20.4 ms: 1.19x faster                                                    |
| xml_etree_generate      | 94.9 ms                                                             | 80.6 ms: 1.18x faster                                                    |
| sympy_expand            | 540 ms                                                              | 460 ms: 1.17x faster                                                     |
| json                    | 5.41 ms                                                             | 4.63 ms: 1.17x faster                                                    |
| sympy_str               | 328 ms                                                              | 284 ms: 1.16x faster                                                     |
| regex_v8                | 24.9 ms                                                             | 21.6 ms: 1.15x faster                                                    |
| djangocms               | 36.3 us                                                             | 32.0 us: 1.13x faster                                                    |
| sqlite_synth            | 2.97 us                                                             | 2.64 us: 1.13x faster                                                    |
| xml_etree_iterparse     | 111 ms                                                              | 99.4 ms: 1.12x faster                                                    |
| sympy_sum               | 185 ms                                                              | 165 ms: 1.12x faster                                                     |
| meteor_contest          | 115 ms                                                              | 103 ms: 1.12x faster                                                     |
| xml_etree_parse         | 164 ms                                                              | 147 ms: 1.11x faster                                                     |
| pathlib                 | 19.8 ms                                                             | 18.1 ms: 1.09x faster                                                    |
| mdp                     | 2.75 sec                                                            | 2.53 sec: 1.09x faster                                                   |
| unpickle                | 15.0 us                                                             | 13.8 us: 1.08x faster                                                    |
| create_gc_cycles        | 1.64 ms                                                             | 1.52 ms: 1.08x faster                                                    |
| pickle_list             | 4.73 us                                                             | 4.43 us: 1.07x faster                                                    |
| regex_dna               | 213 ms                                                              | 204 ms: 1.04x faster                                                     |
| telco                   | 6.67 ms                                                             | 6.47 ms: 1.03x faster                                                    |
| async_generators        | 420 ms                                                              | 413 ms: 1.02x faster                                                     |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                     |
| bench_mp_pool           | 24.0 ms                                                             | 24.0 ms: 1.00x slower                                                    |
| unpickle_list           | 4.94 us                                                             | 5.05 us: 1.02x slower                                                    |
| pickle                  | 10.2 us                                                             | 10.6 us: 1.04x slower                                                    |
| regex_effbot            | 3.22 ms                                                             | 3.41 ms: 1.06x slower                                                    |
| gc_traversal            | 3.53 ms                                                             | 3.97 ms: 1.12x slower                                                    |
| python_startup_no_site  | 5.80 ms                                                             | 6.52 ms: 1.13x slower                                                    |
| pickle_dict             | 27.8 us                                                             | 31.9 us: 1.15x slower                                                    |
| dask                    | 437 ms                                                              | 503 ms: 1.15x slower                                                     |
| coverage                | 70.6 ms                                                             | 96.3 ms: 1.36x slower                                                    |
| Geometric mean          | (ref)                                                               | 1.30x faster                                                             |
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
