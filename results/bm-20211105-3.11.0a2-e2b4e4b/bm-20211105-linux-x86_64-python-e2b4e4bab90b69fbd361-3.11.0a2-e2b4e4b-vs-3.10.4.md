
# Results vs. 3.10.4

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: linux-x86_64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.16x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 274 ms: 1.23x faster                                                  |
| chameleon      | 9.17 ms                                                | 7.46 ms: 1.23x faster                                                 |
| docutils       | 3.18 sec                                               | 2.79 sec: 1.14x faster                                                |
| html5lib       | 85.9 ms                                                | 71.5 ms: 1.20x faster                                                 |
| tornado_http   | 128 ms                                                 | 111 ms: 1.16x faster                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 109 ms                                                 | 83.3 ms: 1.31x faster                                                 |
| nbody          | 144 ms                                                 | 112 ms: 1.28x faster                                                  |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.23x faster                                                  |
| regex_v8       | 25.0 ms                                                | 23.7 ms: 1.06x faster                                                 |
| regex_effbot   | 3.19 ms                                                | 3.26 ms: 1.02x slower                                                 |
| regex_dna      | 214 ms                                                 | 219 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 74.5 ms                                                | 59.6 ms: 1.25x faster                                                 |
| pickle_pure_python   | 452 us                                                 | 364 us: 1.24x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 81.6 ms: 1.15x faster                                                 |
| unpickle_pure_python | 302 us                                                 | 271 us: 1.11x faster                                                  |
| json_loads           | 28.7 us                                                | 25.9 us: 1.11x faster                                                 |
| json_dumps           | 13.4 ms                                                | 12.4 ms: 1.09x faster                                                 |
| xml_etree_parse      | 163 ms                                                 | 158 ms: 1.03x faster                                                  |
| unpickle             | 14.2 us                                                | 13.7 us: 1.03x faster                                                 |
| pickle               | 10.2 us                                                | 10.1 us: 1.01x faster                                                 |
| pickle_list          | 4.72 us                                                | 4.68 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 110 ms: 1.00x faster                                                  |
| pickle_dict          | 27.6 us                                                | 28.6 us: 1.04x slower                                                 |
| unpickle_list        | 4.92 us                                                | 5.13 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 5.78 ms                                                | 5.77 ms: 1.00x faster                                                 |
| python_startup         | 14.1 ms                                                | 14.6 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 24.6 ms: 1.24x faster                                                 |
| django_template | 46.3 ms                                                | 37.9 ms: 1.22x faster                                                 |
| mako            | 14.7 ms                                                | 12.1 ms: 1.21x faster                                                 |
| genshi_xml      | 63.7 ms                                                | 56.1 ms: 1.14x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| logging_silent          | 176 ns                                                 | 117 ns: 1.51x faster                                                  |
| deltablue               | 7.28 ms                                                | 4.86 ms: 1.50x faster                                                 |
| raytrace                | 467 ms                                                 | 326 ms: 1.43x faster                                                  |
| spectral_norm           | 150 ms                                                 | 106 ms: 1.41x faster                                                  |
| scimark_monte_carlo     | 109 ms                                                 | 78.4 ms: 1.38x faster                                                 |
| async_tree_none         | 711 ms                                                 | 518 ms: 1.37x faster                                                  |
| chaos                   | 106 ms                                                 | 77.1 ms: 1.37x faster                                                 |
| unpack_sequence         | 59.4 ns                                                | 43.6 ns: 1.36x faster                                                 |
| richards                | 75.2 ms                                                | 55.7 ms: 1.35x faster                                                 |
| go                      | 226 ms                                                 | 167 ms: 1.35x faster                                                  |
| logging_simple          | 8.10 us                                                | 6.07 us: 1.33x faster                                                 |
| generators              | 76.4 ms                                                | 57.4 ms: 1.33x faster                                                 |
| logging_format          | 8.85 us                                                | 6.71 us: 1.32x faster                                                 |
| float                   | 109 ms                                                 | 83.3 ms: 1.31x faster                                                 |
| crypto_pyaes            | 117 ms                                                 | 90.2 ms: 1.29x faster                                                 |
| nbody                   | 144 ms                                                 | 112 ms: 1.28x faster                                                  |
| deepcopy_memo           | 51.7 us                                                | 40.4 us: 1.28x faster                                                 |
| hexiom                  | 9.43 ms                                                | 7.42 ms: 1.27x faster                                                 |
| async_tree_memoization  | 855 ms                                                 | 676 ms: 1.27x faster                                                  |
| async_tree_io           | 1.78 sec                                               | 1.41 sec: 1.26x faster                                                |
| scimark_sor             | 197 ms                                                 | 156 ms: 1.26x faster                                                  |
| thrift                  | 1.03 ms                                                | 821 us: 1.26x faster                                                  |
| pprint_pformat          | 1.98 sec                                               | 1.58 sec: 1.25x faster                                                |
| xml_etree_process       | 74.5 ms                                                | 59.6 ms: 1.25x faster                                                 |
| pyflate                 | 676 ms                                                 | 541 ms: 1.25x faster                                                  |
| pprint_safe_repr        | 953 ms                                                 | 763 ms: 1.25x faster                                                  |
| genshi_text             | 30.6 ms                                                | 24.6 ms: 1.24x faster                                                 |
| pickle_pure_python      | 452 us                                                 | 364 us: 1.24x faster                                                  |
| gunicorn                | 1.43 ms                                                | 1.15 ms: 1.24x faster                                                 |
| chameleon               | 9.17 ms                                                | 7.46 ms: 1.23x faster                                                 |
| regex_compile           | 177 ms                                                 | 145 ms: 1.23x faster                                                  |
| 2to3                    | 335 ms                                                 | 274 ms: 1.23x faster                                                  |
| django_template         | 46.3 ms                                                | 37.9 ms: 1.22x faster                                                 |
| pycparser               | 1.53 sec                                               | 1.26 sec: 1.22x faster                                                |
| mako                    | 14.7 ms                                                | 12.1 ms: 1.21x faster                                                 |
| html5lib                | 85.9 ms                                                | 71.5 ms: 1.20x faster                                                 |
| scimark_fft             | 421 ms                                                 | 355 ms: 1.19x faster                                                  |
| async_generators        | 426 ms                                                 | 361 ms: 1.18x faster                                                  |
| scimark_lu              | 161 ms                                                 | 136 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 818 ms: 1.16x faster                                                  |
| tornado_http            | 128 ms                                                 | 111 ms: 1.16x faster                                                  |
| deepcopy_reduce         | 3.79 us                                                | 3.27 us: 1.16x faster                                                 |
| xml_etree_generate      | 93.8 ms                                                | 81.6 ms: 1.15x faster                                                 |
| deepcopy                | 438 us                                                 | 382 us: 1.15x faster                                                  |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.8 ms: 1.14x faster                                                 |
| fannkuch                | 488 ms                                                 | 427 ms: 1.14x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 145 ms: 1.14x faster                                                  |
| docutils                | 3.18 sec                                               | 2.79 sec: 1.14x faster                                                |
| genshi_xml              | 63.7 ms                                                | 56.1 ms: 1.14x faster                                                 |
| pylint                  | 532 ms                                                 | 469 ms: 1.14x faster                                                  |
| sqlglot_normalize       | 134 ms                                                 | 119 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.86 ms: 1.12x faster                                                 |
| sqlglot_optimize        | 65.2 ms                                                | 58.4 ms: 1.12x faster                                                 |
| unpickle_pure_python    | 302 us                                                 | 271 us: 1.11x faster                                                  |
| dulwich_log             | 75.8 ms                                                | 68.3 ms: 1.11x faster                                                 |
| flaskblogging           | 8.27 ms                                                | 7.46 ms: 1.11x faster                                                 |
| json_loads              | 28.7 us                                                | 25.9 us: 1.11x faster                                                 |
| coroutines              | 31.6 ms                                                | 28.8 ms: 1.10x faster                                                 |
| nqueens                 | 100 ms                                                 | 91.4 ms: 1.10x faster                                                 |
| json                    | 5.35 ms                                                | 4.91 ms: 1.09x faster                                                 |
| json_dumps              | 13.4 ms                                                | 12.4 ms: 1.09x faster                                                 |
| sympy_integrate         | 24.0 ms                                                | 22.2 ms: 1.08x faster                                                 |
| sympy_sum               | 183 ms                                                 | 170 ms: 1.08x faster                                                  |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.07x faster                                                  |
| sympy_str               | 325 ms                                                 | 306 ms: 1.06x faster                                                  |
| bench_thread_pool       | 946 us                                                 | 892 us: 1.06x faster                                                  |
| sqlite_synth            | 2.92 us                                                | 2.76 us: 1.06x faster                                                 |
| sympy_expand            | 534 ms                                                 | 505 ms: 1.06x faster                                                  |
| regex_v8                | 25.0 ms                                                | 23.7 ms: 1.06x faster                                                 |
| pathlib                 | 20.0 ms                                                | 19.1 ms: 1.05x faster                                                 |
| telco                   | 6.73 ms                                                | 6.50 ms: 1.04x faster                                                 |
| xml_etree_parse         | 163 ms                                                 | 158 ms: 1.03x faster                                                  |
| unpickle                | 14.2 us                                                | 13.7 us: 1.03x faster                                                 |
| sqlglot_transpile       | 2.43 ms                                                | 2.37 ms: 1.02x faster                                                 |
| mdp                     | 2.74 sec                                               | 2.71 sec: 1.01x faster                                                |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                  |
| pickle                  | 10.2 us                                                | 10.1 us: 1.01x faster                                                 |
| pickle_list             | 4.72 us                                                | 4.68 us: 1.01x faster                                                 |
| xml_etree_iterparse     | 111 ms                                                 | 110 ms: 1.00x faster                                                  |
| python_startup_no_site  | 5.78 ms                                                | 5.77 ms: 1.00x faster                                                 |
| sqlglot_parse           | 2.04 ms                                                | 2.06 ms: 1.01x slower                                                 |
| coverage                | 74.7 ms                                                | 75.8 ms: 1.01x slower                                                 |
| regex_effbot            | 3.19 ms                                                | 3.26 ms: 1.02x slower                                                 |
| regex_dna               | 214 ms                                                 | 219 ms: 1.02x slower                                                  |
| python_startup          | 14.1 ms                                                | 14.6 ms: 1.03x slower                                                 |
| pickle_dict             | 27.6 us                                                | 28.6 us: 1.04x slower                                                 |
| unpickle_list           | 4.92 us                                                | 5.13 us: 1.04x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.16x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal, mypy2
