
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.25x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 335 ms                                                 | 264 ms: 1.27x faster                                  |
| chameleon      | 9.17 ms                                                | 6.87 ms: 1.33x faster                                 |
| html5lib       | 85.9 ms                                                | 65.3 ms: 1.32x faster                                 |
| tornado_http   | 128 ms                                                 | 95.4 ms: 1.34x faster                                 |
| Geometric mean | (ref)                                                  | 1.32x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 144 ms                                                 | 95.2 ms: 1.51x faster                                 |
| float          | 109 ms                                                 | 74.4 ms: 1.46x faster                                 |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                  |
| regex_v8       | 25.0 ms                                                | 25.9 ms: 1.03x slower                                 |
| regex_effbot   | 3.19 ms                                                | 3.34 ms: 1.04x slower                                 |
| regex_dna      | 214 ms                                                 | 231 ms: 1.08x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 311 us: 1.45x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 55.2 ms: 1.35x faster                                 |
| unpickle_pure_python | 302 us                                                 | 231 us: 1.31x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 78.5 ms: 1.20x faster                                 |
| json_dumps           | 13.4 ms                                                | 12.5 ms: 1.08x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                  |
| pickle               | 10.2 us                                                | 9.55 us: 1.06x faster                                 |
| xml_etree_parse      | 163 ms                                                 | 157 ms: 1.04x faster                                  |
| pickle_list          | 4.72 us                                                | 4.57 us: 1.03x faster                                 |
| json_loads           | 28.7 us                                                | 28.1 us: 1.02x faster                                 |
| pickle_dict          | 27.6 us                                                | 27.6 us: 1.00x slower                                 |
| unpickle_list        | 4.92 us                                                | 4.97 us: 1.01x slower                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.07 ms: 1.75x faster                                 |
| python_startup_no_site | 5.78 ms                                                | 5.98 ms: 1.04x slower                                 |
| Geometric mean         | (ref)                                                  | 1.30x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.2 ms: 1.44x faster                                 |
| django_template | 46.3 ms                                                | 34.3 ms: 1.35x faster                                 |
| Geometric mean  | (ref)                                                  | 1.40x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.70 ms: 1.97x faster                                 |
| python_startup          | 14.1 ms                                                | 8.07 ms: 1.75x faster                                 |
| logging_silent          | 176 ns                                                 | 104 ns: 1.70x faster                                  |
| scimark_sor             | 197 ms                                                 | 123 ms: 1.60x faster                                  |
| richards                | 75.2 ms                                                | 47.5 ms: 1.58x faster                                 |
| go                      | 226 ms                                                 | 143 ms: 1.58x faster                                  |
| pyflate                 | 676 ms                                                 | 438 ms: 1.54x faster                                  |
| scimark_monte_carlo     | 109 ms                                                 | 70.8 ms: 1.53x faster                                 |
| raytrace                | 467 ms                                                 | 306 ms: 1.53x faster                                  |
| nbody                   | 144 ms                                                 | 95.2 ms: 1.51x faster                                 |
| chaos                   | 106 ms                                                 | 70.2 ms: 1.50x faster                                 |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.48x faster                                  |
| float                   | 109 ms                                                 | 74.4 ms: 1.46x faster                                 |
| pickle_pure_python      | 452 us                                                 | 311 us: 1.45x faster                                  |
| mako                    | 14.7 ms                                                | 10.2 ms: 1.44x faster                                 |
| spectral_norm           | 150 ms                                                 | 105 ms: 1.43x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 82.7 ms: 1.41x faster                                 |
| logging_simple          | 8.10 us                                                | 5.80 us: 1.40x faster                                 |
| logging_format          | 8.85 us                                                | 6.35 us: 1.39x faster                                 |
| hexiom                  | 9.43 ms                                                | 6.84 ms: 1.38x faster                                 |
| thrift                  | 1.03 ms                                                | 762 us: 1.36x faster                                  |
| django_template         | 46.3 ms                                                | 34.3 ms: 1.35x faster                                 |
| xml_etree_process       | 74.5 ms                                                | 55.2 ms: 1.35x faster                                 |
| tornado_http            | 128 ms                                                 | 95.4 ms: 1.34x faster                                 |
| chameleon               | 9.17 ms                                                | 6.87 ms: 1.33x faster                                 |
| unpack_sequence         | 59.4 ns                                                | 44.9 ns: 1.32x faster                                 |
| html5lib                | 85.9 ms                                                | 65.3 ms: 1.32x faster                                 |
| unpickle_pure_python    | 302 us                                                 | 231 us: 1.31x faster                                  |
| regex_compile           | 177 ms                                                 | 137 ms: 1.29x faster                                  |
| 2to3                    | 335 ms                                                 | 264 ms: 1.27x faster                                  |
| scimark_fft             | 421 ms                                                 | 335 ms: 1.26x faster                                  |
| pycparser               | 1.53 sec                                               | 1.24 sec: 1.24x faster                                |
| fannkuch                | 488 ms                                                 | 401 ms: 1.22x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 78.5 ms: 1.20x faster                                 |
| dulwich_log             | 75.8 ms                                                | 63.8 ms: 1.19x faster                                 |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.17x faster                                 |
| nqueens                 | 100 ms                                                 | 85.2 ms: 1.17x faster                                 |
| sqlite_synth            | 2.92 us                                                | 2.51 us: 1.17x faster                                 |
| sympy_sum               | 183 ms                                                 | 160 ms: 1.15x faster                                  |
| sympy_str               | 325 ms                                                 | 287 ms: 1.13x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.85 ms: 1.12x faster                                 |
| sympy_expand            | 534 ms                                                 | 476 ms: 1.12x faster                                  |
| pathlib                 | 20.0 ms                                                | 18.5 ms: 1.08x faster                                 |
| json_dumps              | 13.4 ms                                                | 12.5 ms: 1.08x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                  |
| meteor_contest          | 114 ms                                                 | 107 ms: 1.07x faster                                  |
| pickle                  | 10.2 us                                                | 9.55 us: 1.06x faster                                 |
| json                    | 5.35 ms                                                | 5.07 ms: 1.05x faster                                 |
| xml_etree_parse         | 163 ms                                                 | 157 ms: 1.04x faster                                  |
| pickle_list             | 4.72 us                                                | 4.57 us: 1.03x faster                                 |
| telco                   | 6.73 ms                                                | 6.59 ms: 1.02x faster                                 |
| json_loads              | 28.7 us                                                | 28.1 us: 1.02x faster                                 |
| pickle_dict             | 27.6 us                                                | 27.6 us: 1.00x slower                                 |
| unpickle_list           | 4.92 us                                                | 4.97 us: 1.01x slower                                 |
| regex_v8                | 25.0 ms                                                | 25.9 ms: 1.03x slower                                 |
| python_startup_no_site  | 5.78 ms                                                | 5.98 ms: 1.04x slower                                 |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.34 ms: 1.04x slower                                 |
| regex_dna               | 214 ms                                                 | 231 ms: 1.08x slower                                  |
| Geometric mean          | (ref)                                                  | 1.25x faster                                          |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
