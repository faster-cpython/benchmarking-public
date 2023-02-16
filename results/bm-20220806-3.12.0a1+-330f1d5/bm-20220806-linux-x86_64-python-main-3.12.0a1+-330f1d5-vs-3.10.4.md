
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 330f1d5
- commit date: 2022-08-06
- overall geometric mean: 1.33x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 248 ms: 1.35x faster                                   |
| chameleon      | 9.17 ms                                                | 6.50 ms: 1.41x faster                                  |
| html5lib       | 85.9 ms                                                | 62.6 ms: 1.37x faster                                  |
| tornado_http   | 128 ms                                                 | 91.7 ms: 1.40x faster                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 91.3 ms: 1.58x faster                                  |
| float          | 109 ms                                                 | 74.1 ms: 1.47x faster                                  |
| pidigits       | 190 ms                                                 | 194 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.40x faster                                   |
| regex_v8       | 25.0 ms                                                | 20.8 ms: 1.21x faster                                  |
| regex_dna      | 214 ms                                                 | 203 ms: 1.05x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.50 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 288 us: 1.57x faster                                   |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.51x faster                                   |
| xml_etree_process    | 74.5 ms                                                | 52.2 ms: 1.43x faster                                  |
| json_dumps           | 13.4 ms                                                | 9.51 ms: 1.41x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 75.0 ms: 1.25x faster                                  |
| json_loads           | 28.7 us                                                | 24.6 us: 1.17x faster                                  |
| pickle_list          | 4.72 us                                                | 4.26 us: 1.11x faster                                  |
| unpickle             | 14.2 us                                                | 13.3 us: 1.07x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.04x faster                                   |
| pickle               | 10.2 us                                                | 10.4 us: 1.02x slower                                  |
| unpickle_list        | 4.92 us                                                | 5.06 us: 1.03x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.9 us: 1.16x slower                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.15 ms: 1.73x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.01 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.50 ms: 1.54x faster                                  |
| django_template | 46.3 ms                                                | 32.5 ms: 1.43x faster                                  |
| Geometric mean  | (ref)                                                  | 1.48x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.26x faster                                  |
| logging_silent          | 176 ns                                                 | 89.9 ns: 1.96x faster                                  |
| scimark_sor             | 197 ms                                                 | 110 ms: 1.79x faster                                   |
| python_startup          | 14.1 ms                                                | 8.15 ms: 1.73x faster                                  |
| go                      | 226 ms                                                 | 131 ms: 1.73x faster                                   |
| pyflate                 | 676 ms                                                 | 393 ms: 1.72x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 64.2 ms: 1.69x faster                                  |
| richards                | 75.2 ms                                                | 44.5 ms: 1.69x faster                                  |
| raytrace                | 467 ms                                                 | 278 ms: 1.68x faster                                   |
| crypto_pyaes            | 117 ms                                                 | 72.6 ms: 1.61x faster                                  |
| spectral_norm           | 150 ms                                                 | 93.8 ms: 1.59x faster                                  |
| chaos                   | 106 ms                                                 | 66.8 ms: 1.58x faster                                  |
| nbody                   | 144 ms                                                 | 91.3 ms: 1.58x faster                                  |
| hexiom                  | 9.43 ms                                                | 5.98 ms: 1.58x faster                                  |
| pickle_pure_python      | 452 us                                                 | 288 us: 1.57x faster                                   |
| mako                    | 14.7 ms                                                | 9.50 ms: 1.54x faster                                  |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.52x faster                                   |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.51x faster                                   |
| float                   | 109 ms                                                 | 74.1 ms: 1.47x faster                                  |
| pycparser               | 1.53 sec                                               | 1.04 sec: 1.47x faster                                 |
| xml_etree_process       | 74.5 ms                                                | 52.2 ms: 1.43x faster                                  |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.43x faster                                  |
| logging_simple          | 8.10 us                                                | 5.72 us: 1.42x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.51 ms: 1.41x faster                                  |
| chameleon               | 9.17 ms                                                | 6.50 ms: 1.41x faster                                  |
| regex_compile           | 177 ms                                                 | 127 ms: 1.40x faster                                   |
| tornado_http            | 128 ms                                                 | 91.7 ms: 1.40x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.91 ms: 1.40x faster                                  |
| logging_format          | 8.85 us                                                | 6.34 us: 1.40x faster                                  |
| thrift                  | 1.03 ms                                                | 748 us: 1.38x faster                                   |
| html5lib                | 85.9 ms                                                | 62.6 ms: 1.37x faster                                  |
| scimark_fft             | 421 ms                                                 | 311 ms: 1.36x faster                                   |
| 2to3                    | 335 ms                                                 | 248 ms: 1.35x faster                                   |
| fannkuch                | 488 ms                                                 | 374 ms: 1.30x faster                                   |
| unpack_sequence         | 59.4 ns                                                | 45.9 ns: 1.29x faster                                  |
| nqueens                 | 100 ms                                                 | 79.2 ms: 1.26x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 75.0 ms: 1.25x faster                                  |
| dulwich_log             | 75.8 ms                                                | 61.2 ms: 1.24x faster                                  |
| regex_v8                | 25.0 ms                                                | 20.8 ms: 1.21x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.18x faster                                  |
| json_loads              | 28.7 us                                                | 24.6 us: 1.17x faster                                  |
| sympy_expand            | 534 ms                                                 | 461 ms: 1.16x faster                                   |
| sympy_str               | 325 ms                                                 | 282 ms: 1.15x faster                                   |
| sympy_sum               | 183 ms                                                 | 160 ms: 1.14x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                  |
| json                    | 5.35 ms                                                | 4.70 ms: 1.14x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                  |
| meteor_contest          | 114 ms                                                 | 101 ms: 1.12x faster                                   |
| pickle_list             | 4.72 us                                                | 4.26 us: 1.11x faster                                  |
| unpickle                | 14.2 us                                                | 13.3 us: 1.07x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.06x faster                                   |
| regex_dna               | 214 ms                                                 | 203 ms: 1.05x faster                                   |
| telco                   | 6.73 ms                                                | 6.41 ms: 1.05x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.04x faster                                   |
| pidigits                | 190 ms                                                 | 194 ms: 1.02x slower                                   |
| pickle                  | 10.2 us                                                | 10.4 us: 1.02x slower                                  |
| unpickle_list           | 4.92 us                                                | 5.06 us: 1.03x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.01 ms: 1.04x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.50 ms: 1.10x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.9 us: 1.16x slower                                  |
| Geometric mean          | (ref)                                                  | 1.33x faster                                           |
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
