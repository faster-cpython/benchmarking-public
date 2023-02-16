
# Results vs. 3.10.4

- fork: iritkatriel
- ref: copy_consts
- machine: linux-x86_64
- commit hash: f8449d5
- commit date: 2023-01-18
- overall geometric mean: 1.27x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 257 ms: 1.30x faster                                               |
| chameleon      | 9.17 ms                                                | 6.53 ms: 1.40x faster                                              |
| docutils       | 3.18 sec                                               | 2.59 sec: 1.22x faster                                             |
| html5lib       | 85.9 ms                                                | 61.5 ms: 1.40x faster                                              |
| Geometric mean | (ref)                                                  | 1.33x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.4 ms: 1.54x faster                                              |
| float          | 109 ms                                                 | 73.5 ms: 1.48x faster                                              |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.32x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                               |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.17x faster                                              |
| regex_dna      | 214 ms                                                 | 201 ms: 1.06x faster                                               |
| regex_effbot   | 3.19 ms                                                | 3.41 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                  | 1.12x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 293 us: 1.54x faster                                               |
| unpickle_pure_python | 302 us                                                 | 201 us: 1.50x faster                                               |
| json_dumps           | 13.4 ms                                                | 9.65 ms: 1.39x faster                                              |
| xml_etree_process    | 74.5 ms                                                | 54.6 ms: 1.36x faster                                              |
| xml_etree_generate   | 93.8 ms                                                | 78.6 ms: 1.19x faster                                              |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                              |
| pickle_list          | 4.72 us                                                | 4.03 us: 1.17x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                               |
| unpickle             | 14.2 us                                                | 13.3 us: 1.06x faster                                              |
| pickle               | 10.2 us                                                | 10.2 us: 1.01x slower                                              |
| unpickle_list        | 4.92 us                                                | 4.97 us: 1.01x slower                                              |
| pickle_dict          | 27.6 us                                                | 30.6 us: 1.11x slower                                              |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.56 ms: 1.64x faster                                              |
| python_startup_no_site | 5.78 ms                                                | 6.10 ms: 1.06x slower                                              |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.67 ms: 1.51x faster                                              |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                              |
| django_template | 46.3 ms                                                | 33.8 ms: 1.37x faster                                              |
| genshi_xml      | 63.7 ms                                                | 48.1 ms: 1.33x faster                                              |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.38 ms: 2.15x faster                                              |
| logging_silent          | 176 ns                                                 | 95.0 ns: 1.86x faster                                              |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.83x faster                                               |
| asyncio_tcp             | 914 ms                                                 | 511 ms: 1.79x faster                                               |
| richards                | 75.2 ms                                                | 43.8 ms: 1.72x faster                                              |
| pyflate                 | 676 ms                                                 | 406 ms: 1.67x faster                                               |
| python_startup          | 14.1 ms                                                | 8.56 ms: 1.64x faster                                              |
| go                      | 226 ms                                                 | 139 ms: 1.63x faster                                               |
| scimark_monte_carlo     | 109 ms                                                 | 67.4 ms: 1.61x faster                                              |
| raytrace                | 467 ms                                                 | 293 ms: 1.59x faster                                               |
| crypto_pyaes            | 117 ms                                                 | 74.7 ms: 1.56x faster                                              |
| pickle_pure_python      | 452 us                                                 | 293 us: 1.54x faster                                               |
| nbody                   | 144 ms                                                 | 93.4 ms: 1.54x faster                                              |
| chaos                   | 106 ms                                                 | 68.6 ms: 1.54x faster                                              |
| hexiom                  | 9.43 ms                                                | 6.18 ms: 1.53x faster                                              |
| mako                    | 14.7 ms                                                | 9.67 ms: 1.51x faster                                              |
| spectral_norm           | 150 ms                                                 | 99.0 ms: 1.51x faster                                              |
| unpickle_pure_python    | 302 us                                                 | 201 us: 1.50x faster                                               |
| float                   | 109 ms                                                 | 73.5 ms: 1.48x faster                                              |
| deepcopy_memo           | 51.7 us                                                | 35.1 us: 1.47x faster                                              |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                              |
| scimark_lu              | 161 ms                                                 | 111 ms: 1.45x faster                                               |
| unpack_sequence         | 59.4 ns                                                | 41.6 ns: 1.43x faster                                              |
| sqlglot_parse           | 2.04 ms                                                | 1.45 ms: 1.41x faster                                              |
| chameleon               | 9.17 ms                                                | 6.53 ms: 1.40x faster                                              |
| pprint_pformat          | 1.98 sec                                               | 1.42 sec: 1.40x faster                                             |
| html5lib                | 85.9 ms                                                | 61.5 ms: 1.40x faster                                              |
| json_dumps              | 13.4 ms                                                | 9.65 ms: 1.39x faster                                              |
| sqlglot_transpile       | 2.43 ms                                                | 1.75 ms: 1.38x faster                                              |
| thrift                  | 1.03 ms                                                | 749 us: 1.38x faster                                               |
| pycparser               | 1.53 sec                                               | 1.11 sec: 1.38x faster                                             |
| django_template         | 46.3 ms                                                | 33.8 ms: 1.37x faster                                              |
| xml_etree_process       | 74.5 ms                                                | 54.6 ms: 1.36x faster                                              |
| pprint_safe_repr        | 953 ms                                                 | 700 ms: 1.36x faster                                               |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.03 ms: 1.35x faster                                              |
| async_tree_none         | 711 ms                                                 | 530 ms: 1.34x faster                                               |
| scimark_fft             | 421 ms                                                 | 314 ms: 1.34x faster                                               |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                               |
| logging_simple          | 8.10 us                                                | 6.06 us: 1.34x faster                                              |
| async_tree_io           | 1.78 sec                                               | 1.34 sec: 1.33x faster                                             |
| fannkuch                | 488 ms                                                 | 367 ms: 1.33x faster                                               |
| logging_format          | 8.85 us                                                | 6.66 us: 1.33x faster                                              |
| genshi_xml              | 63.7 ms                                                | 48.1 ms: 1.33x faster                                              |
| 2to3                    | 335 ms                                                 | 257 ms: 1.30x faster                                               |
| deepcopy                | 438 us                                                 | 341 us: 1.28x faster                                               |
| async_tree_memoization  | 855 ms                                                 | 674 ms: 1.27x faster                                               |
| deepcopy_reduce         | 3.79 us                                                | 3.00 us: 1.26x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 757 ms: 1.25x faster                                               |
| sqlglot_optimize        | 65.2 ms                                                | 52.5 ms: 1.24x faster                                              |
| sqlglot_normalize       | 134 ms                                                 | 108 ms: 1.24x faster                                               |
| coroutines              | 31.6 ms                                                | 25.6 ms: 1.24x faster                                              |
| docutils                | 3.18 sec                                               | 2.59 sec: 1.22x faster                                             |
| nqueens                 | 100 ms                                                 | 81.8 ms: 1.22x faster                                              |
| dulwich_log             | 75.8 ms                                                | 63.4 ms: 1.20x faster                                              |
| xml_etree_generate      | 93.8 ms                                                | 78.6 ms: 1.19x faster                                              |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                              |
| async_generators        | 426 ms                                                 | 358 ms: 1.19x faster                                               |
| bench_thread_pool       | 946 us                                                 | 797 us: 1.19x faster                                               |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.17x faster                                              |
| pickle_list             | 4.72 us                                                | 4.03 us: 1.17x faster                                              |
| sqlite_synth            | 2.92 us                                                | 2.56 us: 1.14x faster                                              |
| sympy_expand            | 534 ms                                                 | 469 ms: 1.14x faster                                               |
| json                    | 5.35 ms                                                | 4.70 ms: 1.14x faster                                              |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                              |
| sympy_str               | 325 ms                                                 | 288 ms: 1.13x faster                                               |
| djangocms               | 36.9 us                                                | 32.8 us: 1.12x faster                                              |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                              |
| sympy_integrate         | 24.0 ms                                                | 21.9 ms: 1.10x faster                                              |
| sympy_sum               | 183 ms                                                 | 167 ms: 1.10x faster                                               |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                               |
| mdp                     | 2.74 sec                                               | 2.53 sec: 1.09x faster                                             |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                               |
| telco                   | 6.73 ms                                                | 6.31 ms: 1.07x faster                                              |
| regex_dna               | 214 ms                                                 | 201 ms: 1.06x faster                                               |
| unpickle                | 14.2 us                                                | 13.3 us: 1.06x faster                                              |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                               |
| pickle                  | 10.2 us                                                | 10.2 us: 1.01x slower                                              |
| unpickle_list           | 4.92 us                                                | 4.97 us: 1.01x slower                                              |
| generators              | 76.4 ms                                                | 79.0 ms: 1.03x slower                                              |
| python_startup_no_site  | 5.78 ms                                                | 6.10 ms: 1.06x slower                                              |
| regex_effbot            | 3.19 ms                                                | 3.41 ms: 1.07x slower                                              |
| pickle_dict             | 27.6 us                                                | 30.6 us: 1.11x slower                                              |
| dask                    | 436 ms                                                 | 516 ms: 1.18x slower                                               |
| gc_traversal            | 3.53 ms                                                | 4.30 ms: 1.22x slower                                              |
| coverage                | 74.7 ms                                                | 98.3 ms: 1.31x slower                                              |
| Geometric mean          | (ref)                                                  | 1.27x faster                                                       |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-f8449d5/bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5.json: mypy
