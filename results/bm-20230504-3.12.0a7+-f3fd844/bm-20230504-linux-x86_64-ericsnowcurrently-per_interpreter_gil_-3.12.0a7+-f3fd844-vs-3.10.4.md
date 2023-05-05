
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: linux-x86_64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 272 ms: 1.24x faster                                                              |
| docutils       | 3.19 sec                                                            | 2.74 sec: 1.17x faster                                                            |
| tornado_http   | 129 ms                                                              | 100 ms: 1.29x faster                                                              |
| Geometric mean | (ref)                                                               | 1.23x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 90.1 ms: 1.62x faster                                                             |
| float          | 110 ms                                                              | 82.4 ms: 1.33x faster                                                             |
| pidigits       | 190 ms                                                              | 197 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                               | 1.28x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 146 ms: 1.21x faster                                                              |
| regex_v8       | 24.9 ms                                                             | 22.2 ms: 1.12x faster                                                             |
| regex_dna      | 213 ms                                                              | 204 ms: 1.04x faster                                                              |
| regex_effbot   | 3.22 ms                                                             | 3.66 ms: 1.14x slower                                                             |
| Geometric mean | (ref)                                                               | 1.06x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 320 us: 1.43x faster                                                              |
| unpickle_pure_python | 300 us                                                              | 222 us: 1.35x faster                                                              |
| json_dumps           | 13.7 ms                                                             | 10.1 ms: 1.35x faster                                                             |
| xml_etree_process    | 74.8 ms                                                             | 59.9 ms: 1.25x faster                                                             |
| json_loads           | 29.3 us                                                             | 25.1 us: 1.17x faster                                                             |
| xml_etree_generate   | 94.9 ms                                                             | 85.1 ms: 1.11x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                                              |
| xml_etree_parse      | 164 ms                                                              | 154 ms: 1.07x faster                                                              |
| pickle_list          | 4.73 us                                                             | 4.57 us: 1.04x faster                                                             |
| unpickle             | 15.0 us                                                             | 14.6 us: 1.03x faster                                                             |
| unpickle_list        | 4.94 us                                                             | 4.83 us: 1.02x faster                                                             |
| pickle               | 10.2 us                                                             | 10.7 us: 1.05x slower                                                             |
| pickle_dict          | 27.8 us                                                             | 30.4 us: 1.10x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.12x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.14 ms: 1.55x faster                                                             |
| python_startup_no_site | 5.80 ms                                                             | 6.69 ms: 1.15x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.16x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-----------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                             | 10.6 ms: 1.38x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 31.4 ms: 2.41x faster                                                             |
| deltablue               | 7.30 ms                                                             | 3.54 ms: 2.06x faster                                                             |
| asyncio_tcp             | 922 ms                                                              | 510 ms: 1.81x faster                                                              |
| richards                | 74.2 ms                                                             | 44.1 ms: 1.68x faster                                                             |
| logging_silent          | 169 ns                                                              | 103 ns: 1.64x faster                                                              |
| nbody                   | 146 ms                                                              | 90.1 ms: 1.62x faster                                                             |
| go                      | 226 ms                                                              | 141 ms: 1.60x faster                                                              |
| scimark_sor             | 198 ms                                                              | 124 ms: 1.59x faster                                                              |
| python_startup          | 14.1 ms                                                             | 9.14 ms: 1.55x faster                                                             |
| sqlglot_parse           | 2.07 ms                                                             | 1.34 ms: 1.54x faster                                                             |
| raytrace                | 470 ms                                                              | 307 ms: 1.53x faster                                                              |
| chaos                   | 106 ms                                                              | 70.3 ms: 1.51x faster                                                             |
| pyflate                 | 671 ms                                                              | 446 ms: 1.50x faster                                                              |
| scimark_monte_carlo     | 109 ms                                                              | 73.0 ms: 1.49x faster                                                             |
| crypto_pyaes            | 117 ms                                                              | 78.7 ms: 1.48x faster                                                             |
| hexiom                  | 9.50 ms                                                             | 6.43 ms: 1.48x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                             | 1.67 ms: 1.47x faster                                                             |
| async_tree_io           | 1.78 sec                                                            | 1.23 sec: 1.45x faster                                                            |
| pickle_pure_python      | 457 us                                                              | 320 us: 1.43x faster                                                              |
| async_tree_none         | 713 ms                                                              | 502 ms: 1.42x faster                                                              |
| spectral_norm           | 150 ms                                                              | 108 ms: 1.40x faster                                                              |
| scimark_lu              | 160 ms                                                              | 115 ms: 1.39x faster                                                              |
| async_tree_memoization  | 853 ms                                                              | 616 ms: 1.38x faster                                                              |
| mako                    | 14.7 ms                                                             | 10.6 ms: 1.38x faster                                                             |
| coroutines              | 31.8 ms                                                             | 23.1 ms: 1.38x faster                                                             |
| unpickle_pure_python    | 300 us                                                              | 222 us: 1.35x faster                                                              |
| json_dumps              | 13.7 ms                                                             | 10.1 ms: 1.35x faster                                                             |
| unpack_sequence         | 65.6 ns                                                             | 49.1 ns: 1.34x faster                                                             |
| float                   | 110 ms                                                              | 82.4 ms: 1.33x faster                                                             |
| pycparser               | 1.53 sec                                                            | 1.16 sec: 1.32x faster                                                            |
| deepcopy_memo           | 51.8 us                                                             | 39.3 us: 1.32x faster                                                             |
| pprint_pformat          | 1.98 sec                                                            | 1.52 sec: 1.30x faster                                                            |
| async_tree_cpu_io_mixed | 944 ms                                                              | 726 ms: 1.30x faster                                                              |
| tornado_http            | 129 ms                                                              | 100 ms: 1.29x faster                                                              |
| logging_format          | 9.07 us                                                             | 7.08 us: 1.28x faster                                                             |
| logging_simple          | 8.21 us                                                             | 6.43 us: 1.28x faster                                                             |
| pprint_safe_repr        | 953 ms                                                              | 749 ms: 1.27x faster                                                              |
| fannkuch                | 485 ms                                                              | 383 ms: 1.27x faster                                                              |
| xml_etree_process       | 74.8 ms                                                             | 59.9 ms: 1.25x faster                                                             |
| 2to3                    | 336 ms                                                              | 272 ms: 1.24x faster                                                              |
| mypy2                   | 432 ms                                                              | 353 ms: 1.22x faster                                                              |
| regex_compile           | 177 ms                                                              | 146 ms: 1.21x faster                                                              |
| scimark_fft             | 425 ms                                                              | 355 ms: 1.20x faster                                                              |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.75 ms: 1.18x faster                                                             |
| sqlglot_normalize       | 135 ms                                                              | 114 ms: 1.18x faster                                                              |
| comprehensions          | 27.3 us                                                             | 23.2 us: 1.18x faster                                                             |
| sqlglot_optimize        | 65.3 ms                                                             | 55.5 ms: 1.18x faster                                                             |
| deepcopy                | 438 us                                                              | 374 us: 1.17x faster                                                              |
| json_loads              | 29.3 us                                                             | 25.1 us: 1.17x faster                                                             |
| docutils                | 3.19 sec                                                            | 2.74 sec: 1.17x faster                                                            |
| deepcopy_reduce         | 3.80 us                                                             | 3.26 us: 1.17x faster                                                             |
| nqueens                 | 98.8 ms                                                             | 84.9 ms: 1.16x faster                                                             |
| bench_thread_pool       | 954 us                                                              | 842 us: 1.13x faster                                                              |
| sqlalchemy_declarative  | 166 ms                                                              | 147 ms: 1.13x faster                                                              |
| json                    | 5.41 ms                                                             | 4.82 ms: 1.12x faster                                                             |
| regex_v8                | 24.9 ms                                                             | 22.2 ms: 1.12x faster                                                             |
| create_gc_cycles        | 1.64 ms                                                             | 1.46 ms: 1.12x faster                                                             |
| xml_etree_generate      | 94.9 ms                                                             | 85.1 ms: 1.11x faster                                                             |
| dulwich_log             | 76.3 ms                                                             | 68.5 ms: 1.11x faster                                                             |
| sqlalchemy_imperative   | 21.2 ms                                                             | 19.0 ms: 1.11x faster                                                             |
| sqlite_synth            | 2.97 us                                                             | 2.69 us: 1.10x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                                              |
| xml_etree_parse         | 164 ms                                                              | 154 ms: 1.07x faster                                                              |
| pathlib                 | 19.8 ms                                                             | 18.6 ms: 1.06x faster                                                             |
| mdp                     | 2.75 sec                                                            | 2.61 sec: 1.06x faster                                                            |
| regex_dna               | 213 ms                                                              | 204 ms: 1.04x faster                                                              |
| pickle_list             | 4.73 us                                                             | 4.57 us: 1.04x faster                                                             |
| unpickle                | 15.0 us                                                             | 14.6 us: 1.03x faster                                                             |
| unpickle_list           | 4.94 us                                                             | 4.83 us: 1.02x faster                                                             |
| bench_mp_pool           | 24.0 ms                                                             | 24.0 ms: 1.00x slower                                                             |
| telco                   | 6.67 ms                                                             | 6.84 ms: 1.03x slower                                                             |
| meteor_contest          | 115 ms                                                              | 118 ms: 1.03x slower                                                              |
| pidigits                | 190 ms                                                              | 197 ms: 1.04x slower                                                              |
| pickle                  | 10.2 us                                                             | 10.7 us: 1.05x slower                                                             |
| async_generators        | 420 ms                                                              | 450 ms: 1.07x slower                                                              |
| pickle_dict             | 27.8 us                                                             | 30.4 us: 1.10x slower                                                             |
| regex_effbot            | 3.22 ms                                                             | 3.66 ms: 1.14x slower                                                             |
| gc_traversal            | 3.53 ms                                                             | 4.04 ms: 1.15x slower                                                             |
| python_startup_no_site  | 5.80 ms                                                             | 6.69 ms: 1.15x slower                                                             |
| dask                    | 437 ms                                                              | 543 ms: 1.24x slower                                                              |
| coverage                | 70.6 ms                                                             | 102 ms: 1.45x slower                                                              |
| Geometric mean          | (ref)                                                               | 1.23x faster                                                                      |
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
