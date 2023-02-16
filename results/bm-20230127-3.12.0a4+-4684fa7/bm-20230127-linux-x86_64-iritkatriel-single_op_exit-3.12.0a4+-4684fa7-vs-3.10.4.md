
# Results vs. 3.10.4

- fork: iritkatriel
- ref: single_op_exit
- machine: linux-x86_64
- commit hash: 4684fa7
- commit date: 2023-01-27
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                                  |
| chameleon      | 9.17 ms                                                | 6.53 ms: 1.40x faster                                                 |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                |
| html5lib       | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                 |
| tornado_http   | 128 ms                                                 | 93.0 ms: 1.38x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 95.1 ms: 1.51x faster                                                 |
| float          | 109 ms                                                 | 72.8 ms: 1.50x faster                                                 |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                                  |
| regex_dna      | 214 ms                                                 | 209 ms: 1.02x faster                                                  |
| regex_v8       | 25.0 ms                                                | 25.9 ms: 1.03x slower                                                 |
| regex_effbot   | 3.19 ms                                                | 3.57 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 283 us: 1.60x faster                                                  |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                  |
| json_dumps           | 13.4 ms                                                | 9.28 ms: 1.45x faster                                                 |
| xml_etree_process    | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                 |
| xml_etree_generate   | 93.8 ms                                                | 77.6 ms: 1.21x faster                                                 |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                                 |
| pickle_list          | 4.72 us                                                | 4.21 us: 1.12x faster                                                 |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                  |
| unpickle             | 14.2 us                                                | 13.3 us: 1.06x faster                                                 |
| unpickle_list        | 4.92 us                                                | 4.98 us: 1.01x slower                                                 |
| pickle_dict          | 27.6 us                                                | 31.1 us: 1.13x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                          |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.96 ms: 1.57x faster                                                 |
| python_startup_no_site | 5.78 ms                                                | 6.48 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.69 ms: 1.51x faster                                                 |
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                 |
| django_template | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                 |
| genshi_xml      | 63.7 ms                                                | 46.1 ms: 1.38x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.26 ms: 2.23x faster                                                 |
| logging_silent          | 176 ns                                                 | 92.0 ns: 1.92x faster                                                 |
| asyncio_tcp             | 914 ms                                                 | 496 ms: 1.84x faster                                                  |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.83x faster                                                  |
| richards                | 75.2 ms                                                | 42.1 ms: 1.79x faster                                                 |
| pyflate                 | 676 ms                                                 | 399 ms: 1.69x faster                                                  |
| scimark_monte_carlo     | 109 ms                                                 | 64.2 ms: 1.69x faster                                                 |
| raytrace                | 467 ms                                                 | 281 ms: 1.66x faster                                                  |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                                  |
| chaos                   | 106 ms                                                 | 64.8 ms: 1.63x faster                                                 |
| pickle_pure_python      | 452 us                                                 | 283 us: 1.60x faster                                                  |
| crypto_pyaes            | 117 ms                                                 | 73.3 ms: 1.59x faster                                                 |
| hexiom                  | 9.43 ms                                                | 5.94 ms: 1.59x faster                                                 |
| python_startup          | 14.1 ms                                                | 8.96 ms: 1.57x faster                                                 |
| spectral_norm           | 150 ms                                                 | 96.5 ms: 1.55x faster                                                 |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                  |
| mako                    | 14.7 ms                                                | 9.69 ms: 1.51x faster                                                 |
| nbody                   | 144 ms                                                 | 95.1 ms: 1.51x faster                                                 |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.51x faster                                                  |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                 |
| float                   | 109 ms                                                 | 72.8 ms: 1.50x faster                                                 |
| deepcopy_memo           | 51.7 us                                                | 34.7 us: 1.49x faster                                                 |
| json_dumps              | 13.4 ms                                                | 9.28 ms: 1.45x faster                                                 |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                                 |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.43x faster                                                |
| html5lib                | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                 |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                 |
| logging_simple          | 8.10 us                                                | 5.70 us: 1.42x faster                                                 |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                                 |
| logging_format          | 8.85 us                                                | 6.25 us: 1.42x faster                                                 |
| pprint_safe_repr        | 953 ms                                                 | 674 ms: 1.41x faster                                                  |
| chameleon               | 9.17 ms                                                | 6.53 ms: 1.40x faster                                                 |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.40x faster                                                |
| scimark_fft             | 421 ms                                                 | 301 ms: 1.40x faster                                                  |
| unpack_sequence         | 59.4 ns                                                | 42.8 ns: 1.39x faster                                                 |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                                  |
| genshi_xml              | 63.7 ms                                                | 46.1 ms: 1.38x faster                                                 |
| tornado_http            | 128 ms                                                 | 93.0 ms: 1.38x faster                                                 |
| xml_etree_process       | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                 |
| thrift                  | 1.03 ms                                                | 755 us: 1.37x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.99 ms: 1.37x faster                                                 |
| async_tree_none         | 711 ms                                                 | 525 ms: 1.35x faster                                                  |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.35x faster                                                 |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                |
| aiohttp                 | 1.34 ms                                                | 991 us: 1.35x faster                                                  |
| async_tree_memoization  | 855 ms                                                 | 633 ms: 1.35x faster                                                  |
| deepcopy                | 438 us                                                 | 327 us: 1.34x faster                                                  |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                                  |
| nqueens                 | 100 ms                                                 | 76.8 ms: 1.30x faster                                                 |
| fannkuch                | 488 ms                                                 | 377 ms: 1.29x faster                                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.93 us: 1.29x faster                                                 |
| sqlglot_optimize        | 65.2 ms                                                | 50.6 ms: 1.29x faster                                                 |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                  |
| coroutines              | 31.6 ms                                                | 24.8 ms: 1.27x faster                                                 |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                |
| async_tree_cpu_io_mixed | 949 ms                                                 | 757 ms: 1.25x faster                                                  |
| bench_thread_pool       | 946 us                                                 | 769 us: 1.23x faster                                                  |
| dulwich_log             | 75.8 ms                                                | 61.8 ms: 1.23x faster                                                 |
| sympy_integrate         | 24.0 ms                                                | 19.7 ms: 1.22x faster                                                 |
| sympy_str               | 325 ms                                                 | 268 ms: 1.21x faster                                                  |
| xml_etree_generate      | 93.8 ms                                                | 77.6 ms: 1.21x faster                                                 |
| async_generators        | 426 ms                                                 | 354 ms: 1.20x faster                                                  |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                                 |
| sympy_sum               | 183 ms                                                 | 154 ms: 1.19x faster                                                  |
| sympy_expand            | 534 ms                                                 | 452 ms: 1.18x faster                                                  |
| json                    | 5.35 ms                                                | 4.61 ms: 1.16x faster                                                 |
| sqlite_synth            | 2.92 us                                                | 2.57 us: 1.14x faster                                                 |
| djangocms               | 36.9 us                                                | 32.7 us: 1.13x faster                                                 |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                 |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                                 |
| pickle_list             | 4.72 us                                                | 4.21 us: 1.12x faster                                                 |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                  |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.08x faster                                                  |
| telco                   | 6.73 ms                                                | 6.28 ms: 1.07x faster                                                 |
| unpickle                | 14.2 us                                                | 13.3 us: 1.06x faster                                                 |
| regex_dna               | 214 ms                                                 | 209 ms: 1.02x faster                                                  |
| mdp                     | 2.74 sec                                               | 2.69 sec: 1.02x faster                                                |
| generators              | 76.4 ms                                                | 74.9 ms: 1.02x faster                                                 |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                  |
| unpickle_list           | 4.92 us                                                | 4.98 us: 1.01x slower                                                 |
| regex_v8                | 25.0 ms                                                | 25.9 ms: 1.03x slower                                                 |
| regex_effbot            | 3.19 ms                                                | 3.57 ms: 1.12x slower                                                 |
| python_startup_no_site  | 5.78 ms                                                | 6.48 ms: 1.12x slower                                                 |
| dask                    | 436 ms                                                 | 491 ms: 1.13x slower                                                  |
| pickle_dict             | 27.6 us                                                | 31.1 us: 1.13x slower                                                 |
| gc_traversal            | 3.53 ms                                                | 4.30 ms: 1.22x slower                                                 |
| coverage                | 74.7 ms                                                | 97.8 ms: 1.31x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230127-3.12.0a4+-4684fa7/bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7.json: mypy
