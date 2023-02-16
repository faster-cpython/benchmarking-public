
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: b0e1f9c
- commit date: 2022-11-19
- overall geometric mean: 1.32x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 245 ms: 1.37x faster                                   |
| chameleon      | 9.17 ms                                                | 6.49 ms: 1.41x faster                                  |
| html5lib       | 85.9 ms                                                | 59.1 ms: 1.45x faster                                  |
| tornado_http   | 128 ms                                                 | 92.7 ms: 1.38x faster                                  |
| Geometric mean | (ref)                                                  | 1.40x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.1 ms: 1.53x faster                                  |
| float          | 109 ms                                                 | 71.6 ms: 1.52x faster                                  |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| regex_dna      | 214 ms                                                 | 213 ms: 1.01x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.77 ms: 1.18x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 283 us: 1.60x faster                                   |
| unpickle_pure_python | 302 us                                                 | 201 us: 1.50x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.42 ms: 1.43x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 52.9 ms: 1.41x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 76.4 ms: 1.23x faster                                  |
| json_loads           | 28.7 us                                                | 24.2 us: 1.19x faster                                  |
| pickle_list          | 4.72 us                                                | 4.11 us: 1.15x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| unpickle             | 14.2 us                                                | 13.6 us: 1.04x faster                                  |
| unpickle_list        | 4.92 us                                                | 5.10 us: 1.04x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.0 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.51 ms: 1.65x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.25 ms: 1.08x slower                                  |
| Geometric mean         | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                  |
| mako            | 14.7 ms                                                | 9.94 ms: 1.47x faster                                  |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                  |
| genshi_xml      | 63.7 ms                                                | 46.2 ms: 1.38x faster                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.23 ms: 2.25x faster                                  |
| logging_silent          | 176 ns                                                 | 91.1 ns: 1.94x faster                                  |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.89x faster                                   |
| richards                | 75.2 ms                                                | 41.6 ms: 1.81x faster                                  |
| scimark_monte_carlo     | 109 ms                                                 | 64.0 ms: 1.69x faster                                  |
| pyflate                 | 676 ms                                                 | 403 ms: 1.68x faster                                   |
| raytrace                | 467 ms                                                 | 278 ms: 1.68x faster                                   |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                   |
| python_startup          | 14.1 ms                                                | 8.51 ms: 1.65x faster                                  |
| chaos                   | 106 ms                                                 | 66.0 ms: 1.60x faster                                  |
| pickle_pure_python      | 452 us                                                 | 283 us: 1.60x faster                                   |
| crypto_pyaes            | 117 ms                                                 | 74.3 ms: 1.57x faster                                  |
| scimark_lu              | 161 ms                                                 | 104 ms: 1.55x faster                                   |
| sqlglot_parse           | 2.04 ms                                                | 1.33 ms: 1.54x faster                                  |
| spectral_norm           | 150 ms                                                 | 97.6 ms: 1.53x faster                                  |
| nbody                   | 144 ms                                                 | 94.1 ms: 1.53x faster                                  |
| float                   | 109 ms                                                 | 71.6 ms: 1.52x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.21 ms: 1.52x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 34.2 us: 1.51x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.61 ms: 1.50x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 201 us: 1.50x faster                                   |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                  |
| mako                    | 14.7 ms                                                | 9.94 ms: 1.47x faster                                  |
| html5lib                | 85.9 ms                                                | 59.1 ms: 1.45x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                 |
| json_dumps              | 13.4 ms                                                | 9.42 ms: 1.43x faster                                  |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                  |
| pprint_safe_repr        | 953 ms                                                 | 673 ms: 1.42x faster                                   |
| chameleon               | 9.17 ms                                                | 6.49 ms: 1.41x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 52.9 ms: 1.41x faster                                  |
| logging_simple          | 8.10 us                                                | 5.77 us: 1.40x faster                                  |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                   |
| logging_format          | 8.85 us                                                | 6.35 us: 1.39x faster                                  |
| scimark_fft             | 421 ms                                                 | 303 ms: 1.39x faster                                   |
| thrift                  | 1.03 ms                                                | 746 us: 1.39x faster                                   |
| unpack_sequence         | 59.4 ns                                                | 42.9 ns: 1.38x faster                                  |
| tornado_http            | 128 ms                                                 | 92.7 ms: 1.38x faster                                  |
| genshi_xml              | 63.7 ms                                                | 46.2 ms: 1.38x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.96 ms: 1.38x faster                                  |
| 2to3                    | 335 ms                                                 | 245 ms: 1.37x faster                                   |
| pycparser               | 1.53 sec                                               | 1.12 sec: 1.37x faster                                 |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                 |
| async_tree_none         | 711 ms                                                 | 527 ms: 1.35x faster                                   |
| aiohttp                 | 1.34 ms                                                | 999 us: 1.34x faster                                   |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                  |
| deepcopy                | 438 us                                                 | 330 us: 1.33x faster                                   |
| fannkuch                | 488 ms                                                 | 369 ms: 1.32x faster                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 729 ms: 1.30x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.7 ms: 1.29x faster                                  |
| async_tree_memoization  | 855 ms                                                 | 665 ms: 1.29x faster                                   |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                   |
| coroutines              | 31.6 ms                                                | 24.8 ms: 1.27x faster                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.98 us: 1.27x faster                                  |
| dulwich_log             | 75.8 ms                                                | 60.6 ms: 1.25x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 76.4 ms: 1.23x faster                                  |
| nqueens                 | 100 ms                                                 | 81.5 ms: 1.23x faster                                  |
| json_loads              | 28.7 us                                                | 24.2 us: 1.19x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                  |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                   |
| pickle_list             | 4.72 us                                                | 4.11 us: 1.15x faster                                  |
| sympy_str               | 325 ms                                                 | 283 ms: 1.15x faster                                   |
| json                    | 5.35 ms                                                | 4.67 ms: 1.14x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.14x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| sympy_sum               | 183 ms                                                 | 165 ms: 1.11x faster                                   |
| sqlite_synth            | 2.92 us                                                | 2.64 us: 1.11x faster                                  |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| telco                   | 6.73 ms                                                | 6.27 ms: 1.07x faster                                  |
| unpickle                | 14.2 us                                                | 13.6 us: 1.04x faster                                  |
| mdp                     | 2.74 sec                                               | 2.65 sec: 1.04x faster                                 |
| regex_dna               | 214 ms                                                 | 213 ms: 1.01x faster                                   |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                   |
| generators              | 76.4 ms                                                | 78.0 ms: 1.02x slower                                  |
| unpickle_list           | 4.92 us                                                | 5.10 us: 1.04x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.25 ms: 1.08x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.0 us: 1.12x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.77 ms: 1.18x slower                                  |
| coverage                | 74.7 ms                                                | 98.2 ms: 1.31x slower                                  |
| Geometric mean          | (ref)                                                  | 1.32x faster                                           |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221119-3.12.0a3+-b0e1f9c/bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c.json: mypy
