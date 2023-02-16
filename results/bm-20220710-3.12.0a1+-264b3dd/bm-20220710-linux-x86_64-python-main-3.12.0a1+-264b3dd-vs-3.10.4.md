
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 264b3dd
- commit date: 2022-07-10
- overall geometric mean: 1.32x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 249 ms: 1.35x faster                                   |
| chameleon      | 9.17 ms                                                | 6.30 ms: 1.46x faster                                  |
| html5lib       | 85.9 ms                                                | 62.6 ms: 1.37x faster                                  |
| tornado_http   | 128 ms                                                 | 91.3 ms: 1.40x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 90.5 ms: 1.59x faster                                  |
| float          | 109 ms                                                 | 72.4 ms: 1.51x faster                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 126 ms: 1.41x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                  |
| regex_dna      | 214 ms                                                 | 207 ms: 1.03x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.54 ms: 1.11x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 286 us: 1.58x faster                                   |
| unpickle_pure_python | 302 us                                                 | 201 us: 1.50x faster                                   |
| xml_etree_process    | 74.5 ms                                                | 53.3 ms: 1.40x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 75.9 ms: 1.24x faster                                  |
| json_loads           | 28.7 us                                                | 24.2 us: 1.18x faster                                  |
| pickle_list          | 4.72 us                                                | 4.12 us: 1.15x faster                                  |
| json_dumps           | 13.4 ms                                                | 11.8 ms: 1.14x faster                                  |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.04x faster                                   |
| unpickle_list        | 4.92 us                                                | 5.04 us: 1.02x slower                                  |
| pickle               | 10.2 us                                                | 10.5 us: 1.03x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.6 us: 1.15x slower                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.16 ms: 1.73x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.01 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.45 ms: 1.55x faster                                  |
| django_template | 46.3 ms                                                | 31.5 ms: 1.47x faster                                  |
| Geometric mean  | (ref)                                                  | 1.51x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.24 ms: 2.25x faster                                  |
| logging_silent          | 176 ns                                                 | 92.5 ns: 1.91x faster                                  |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.78x faster                                   |
| go                      | 226 ms                                                 | 130 ms: 1.74x faster                                   |
| python_startup          | 14.1 ms                                                | 8.16 ms: 1.73x faster                                  |
| pyflate                 | 676 ms                                                 | 398 ms: 1.70x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 64.6 ms: 1.68x faster                                  |
| richards                | 75.2 ms                                                | 45.0 ms: 1.67x faster                                  |
| raytrace                | 467 ms                                                 | 286 ms: 1.63x faster                                   |
| chaos                   | 106 ms                                                 | 65.0 ms: 1.62x faster                                  |
| hexiom                  | 9.43 ms                                                | 5.92 ms: 1.59x faster                                  |
| nbody                   | 144 ms                                                 | 90.5 ms: 1.59x faster                                  |
| pickle_pure_python      | 452 us                                                 | 286 us: 1.58x faster                                   |
| crypto_pyaes            | 117 ms                                                 | 74.3 ms: 1.57x faster                                  |
| mako                    | 14.7 ms                                                | 9.45 ms: 1.55x faster                                  |
| scimark_lu              | 161 ms                                                 | 104 ms: 1.54x faster                                   |
| spectral_norm           | 150 ms                                                 | 97.7 ms: 1.53x faster                                  |
| float                   | 109 ms                                                 | 72.4 ms: 1.51x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 201 us: 1.50x faster                                   |
| django_template         | 46.3 ms                                                | 31.5 ms: 1.47x faster                                  |
| chameleon               | 9.17 ms                                                | 6.30 ms: 1.46x faster                                  |
| pycparser               | 1.53 sec                                               | 1.06 sec: 1.44x faster                                 |
| thrift                  | 1.03 ms                                                | 720 us: 1.44x faster                                   |
| logging_simple          | 8.10 us                                                | 5.67 us: 1.43x faster                                  |
| regex_compile           | 177 ms                                                 | 126 ms: 1.41x faster                                   |
| tornado_http            | 128 ms                                                 | 91.3 ms: 1.40x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 53.3 ms: 1.40x faster                                  |
| logging_format          | 8.85 us                                                | 6.35 us: 1.40x faster                                  |
| html5lib                | 85.9 ms                                                | 62.6 ms: 1.37x faster                                  |
| 2to3                    | 335 ms                                                 | 249 ms: 1.35x faster                                   |
| scimark_fft             | 421 ms                                                 | 313 ms: 1.35x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.18 ms: 1.31x faster                                  |
| fannkuch                | 488 ms                                                 | 378 ms: 1.29x faster                                   |
| unpack_sequence         | 59.4 ns                                                | 46.4 ns: 1.28x faster                                  |
| dulwich_log             | 75.8 ms                                                | 61.2 ms: 1.24x faster                                  |
| nqueens                 | 100 ms                                                 | 80.8 ms: 1.24x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 75.9 ms: 1.24x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.1 ms: 1.20x faster                                  |
| sympy_expand            | 534 ms                                                 | 450 ms: 1.19x faster                                   |
| json_loads              | 28.7 us                                                | 24.2 us: 1.18x faster                                  |
| sympy_str               | 325 ms                                                 | 279 ms: 1.17x faster                                   |
| sympy_sum               | 183 ms                                                 | 158 ms: 1.16x faster                                   |
| pickle_list             | 4.72 us                                                | 4.12 us: 1.15x faster                                  |
| json                    | 5.35 ms                                                | 4.69 ms: 1.14x faster                                  |
| json_dumps              | 13.4 ms                                                | 11.8 ms: 1.14x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.1 ms: 1.13x faster                                  |
| meteor_contest          | 114 ms                                                 | 101 ms: 1.13x faster                                   |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.12x faster                                  |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                  |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.04x faster                                   |
| telco                   | 6.73 ms                                                | 6.51 ms: 1.03x faster                                  |
| regex_dna               | 214 ms                                                 | 207 ms: 1.03x faster                                   |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                   |
| unpickle_list           | 4.92 us                                                | 5.04 us: 1.02x slower                                  |
| pickle                  | 10.2 us                                                | 10.5 us: 1.03x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.01 ms: 1.04x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.54 ms: 1.11x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.6 us: 1.15x slower                                  |
| Geometric mean          | (ref)                                                  | 1.32x faster                                           |
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
