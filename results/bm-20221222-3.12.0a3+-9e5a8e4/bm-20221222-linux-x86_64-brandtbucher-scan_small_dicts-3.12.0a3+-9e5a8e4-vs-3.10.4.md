
# Results vs. 3.10.4

- fork: brandtbucher
- ref: scan_small_dicts
- machine: linux-x86_64
- commit hash: 9e5a8e4
- commit date: 2022-12-22
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 255 ms: 1.32x faster                                                     |
| chameleon      | 9.17 ms                                                | 6.52 ms: 1.41x faster                                                    |
| docutils       | 3.18 sec                                               | 2.65 sec: 1.20x faster                                                   |
| html5lib       | 85.9 ms                                                | 60.4 ms: 1.42x faster                                                    |
| Geometric mean | (ref)                                                  | 1.33x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 109 ms                                                 | 72.2 ms: 1.51x faster                                                    |
| nbody          | 144 ms                                                 | 96.6 ms: 1.49x faster                                                    |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.30x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.36x faster                                                     |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                    |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                     |
| regex_effbot   | 3.19 ms                                                | 3.58 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 285 us: 1.59x faster                                                     |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.52x faster                                                     |
| json_dumps           | 13.4 ms                                                | 9.43 ms: 1.43x faster                                                    |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                    |
| xml_etree_generate   | 93.8 ms                                                | 76.3 ms: 1.23x faster                                                    |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                                    |
| pickle_list          | 4.72 us                                                | 4.09 us: 1.15x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.04x faster                                                     |
| unpickle             | 14.2 us                                                | 13.8 us: 1.03x faster                                                    |
| unpickle_list        | 4.92 us                                                | 5.03 us: 1.02x slower                                                    |
| pickle_dict          | 27.6 us                                                | 30.4 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.55 ms: 1.65x faster                                                    |
| python_startup_no_site | 5.78 ms                                                | 6.13 ms: 1.06x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.37 ms: 1.56x faster                                                    |
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                    |
| django_template | 46.3 ms                                                | 32.0 ms: 1.45x faster                                                    |
| genshi_xml      | 63.7 ms                                                | 47.1 ms: 1.35x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                                    |
| logging_silent          | 176 ns                                                 | 90.9 ns: 1.94x faster                                                    |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.90x faster                                                     |
| pyflate                 | 676 ms                                                 | 399 ms: 1.69x faster                                                     |
| raytrace                | 467 ms                                                 | 278 ms: 1.68x faster                                                     |
| richards                | 75.2 ms                                                | 45.6 ms: 1.65x faster                                                    |
| python_startup          | 14.1 ms                                                | 8.55 ms: 1.65x faster                                                    |
| go                      | 226 ms                                                 | 141 ms: 1.60x faster                                                     |
| scimark_monte_carlo     | 109 ms                                                 | 67.8 ms: 1.60x faster                                                    |
| pickle_pure_python      | 452 us                                                 | 285 us: 1.59x faster                                                     |
| chaos                   | 106 ms                                                 | 67.0 ms: 1.58x faster                                                    |
| hexiom                  | 9.43 ms                                                | 6.02 ms: 1.57x faster                                                    |
| mako                    | 14.7 ms                                                | 9.37 ms: 1.56x faster                                                    |
| deepcopy_memo           | 51.7 us                                                | 33.2 us: 1.56x faster                                                    |
| spectral_norm           | 150 ms                                                 | 97.1 ms: 1.54x faster                                                    |
| crypto_pyaes            | 117 ms                                                 | 75.8 ms: 1.54x faster                                                    |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.52x faster                                                     |
| float                   | 109 ms                                                 | 72.2 ms: 1.51x faster                                                    |
| nbody                   | 144 ms                                                 | 96.6 ms: 1.49x faster                                                    |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                                     |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                    |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.45x faster                                                   |
| django_template         | 46.3 ms                                                | 32.0 ms: 1.45x faster                                                    |
| pprint_safe_repr        | 953 ms                                                 | 665 ms: 1.43x faster                                                     |
| logging_simple          | 8.10 us                                                | 5.68 us: 1.43x faster                                                    |
| json_dumps              | 13.4 ms                                                | 9.43 ms: 1.43x faster                                                    |
| html5lib                | 85.9 ms                                                | 60.4 ms: 1.42x faster                                                    |
| sqlglot_parse           | 2.04 ms                                                | 1.44 ms: 1.42x faster                                                    |
| logging_format          | 8.85 us                                                | 6.28 us: 1.41x faster                                                    |
| chameleon               | 9.17 ms                                                | 6.52 ms: 1.41x faster                                                    |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                    |
| sqlglot_transpile       | 2.43 ms                                                | 1.73 ms: 1.40x faster                                                    |
| unpack_sequence         | 59.4 ns                                                | 42.6 ns: 1.39x faster                                                    |
| regex_compile           | 177 ms                                                 | 131 ms: 1.36x faster                                                     |
| thrift                  | 1.03 ms                                                | 763 us: 1.36x faster                                                     |
| genshi_xml              | 63.7 ms                                                | 47.1 ms: 1.35x faster                                                    |
| scimark_fft             | 421 ms                                                 | 312 ms: 1.35x faster                                                     |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                                   |
| deepcopy                | 438 us                                                 | 329 us: 1.33x faster                                                     |
| pycparser               | 1.53 sec                                               | 1.16 sec: 1.32x faster                                                   |
| 2to3                    | 335 ms                                                 | 255 ms: 1.32x faster                                                     |
| fannkuch                | 488 ms                                                 | 371 ms: 1.32x faster                                                     |
| async_tree_none         | 711 ms                                                 | 541 ms: 1.31x faster                                                     |
| deepcopy_reduce         | 3.79 us                                                | 2.91 us: 1.30x faster                                                    |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.20 ms: 1.30x faster                                                    |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                     |
| sqlglot_optimize        | 65.2 ms                                                | 50.7 ms: 1.29x faster                                                    |
| nqueens                 | 100 ms                                                 | 78.7 ms: 1.27x faster                                                    |
| coroutines              | 31.6 ms                                                | 24.9 ms: 1.27x faster                                                    |
| async_tree_memoization  | 855 ms                                                 | 683 ms: 1.25x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 769 ms: 1.23x faster                                                     |
| xml_etree_generate      | 93.8 ms                                                | 76.3 ms: 1.23x faster                                                    |
| dulwich_log             | 75.8 ms                                                | 62.2 ms: 1.22x faster                                                    |
| bench_thread_pool       | 946 us                                                 | 780 us: 1.21x faster                                                     |
| async_generators        | 426 ms                                                 | 352 ms: 1.21x faster                                                     |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                                    |
| docutils                | 3.18 sec                                               | 2.65 sec: 1.20x faster                                                   |
| sympy_expand            | 534 ms                                                 | 456 ms: 1.17x faster                                                     |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.17x faster                                                    |
| pickle_list             | 4.72 us                                                | 4.09 us: 1.15x faster                                                    |
| pathlib                 | 20.0 ms                                                | 17.4 ms: 1.15x faster                                                    |
| sympy_str               | 325 ms                                                 | 285 ms: 1.14x faster                                                     |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                                    |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                                    |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                    |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.10x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                     |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                                     |
| telco                   | 6.73 ms                                                | 6.31 ms: 1.07x faster                                                    |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.04x faster                                                     |
| json                    | 5.35 ms                                                | 5.17 ms: 1.03x faster                                                    |
| unpickle                | 14.2 us                                                | 13.8 us: 1.03x faster                                                    |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                     |
| mdp                     | 2.74 sec                                               | 2.73 sec: 1.01x faster                                                   |
| generators              | 76.4 ms                                                | 76.8 ms: 1.01x slower                                                    |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                     |
| unpickle_list           | 4.92 us                                                | 5.03 us: 1.02x slower                                                    |
| python_startup_no_site  | 5.78 ms                                                | 6.13 ms: 1.06x slower                                                    |
| pickle_dict             | 27.6 us                                                | 30.4 us: 1.10x slower                                                    |
| regex_effbot            | 3.19 ms                                                | 3.58 ms: 1.12x slower                                                    |
| coverage                | 74.7 ms                                                | 104 ms: 1.39x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                             |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221222-3.12.0a3+-9e5a8e4/bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4.json: mypy
